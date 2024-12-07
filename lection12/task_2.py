# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import log, info, delay


class AuthPage(Region):
    login_field = TextField(By.CSS_SELECTOR, '[type="text"]', 'Логин')
    password_field = TextField(By.CSS_SELECTOR, '[type="password"]', 'Пароль')


class TasksInWorkPage(Region):
    create_btn = Button(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]', 'Кнопка +')
    folder_plus = Button(By.XPATH, '//span[text()="Папка"]', '+ Папка')
    input_name_folder = TextField(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]', 'Название новой папки')
    save_folder = Button(By.CSS_SELECTOR, '.edws-UserFolderDialog__buttonSave', 'Сохранить папку')
    delete_btn = Button(By.CSS_SELECTOR, '[title="Удалить папку"]', 'Удалить папку')
    yes_delete = Button(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Подтвердить удаление')
    folders = CustomList(By.CSS_SELECTOR, '.controls-ListEditor__columns', 'Папки')
    empty_folder = Element(By.CSS_SELECTOR, '[data-qa="hint-EmptyView__title"]', 'Заглушка в реестре')
    active_folder = Element(By.CSS_SELECTOR, '.controls-Grid__row-cell_selected-master', 'Текущая папка')
    marker = Element(By.CSS_SELECTOR, '[data-qa="marker"]', 'Маркер')


class Test(TestCaseUI):

    def test(self):
        auth_link = self.config.get('AUTH_SITE')
        login = self.config.get('USER_LOGIN')
        password = self.config.get('USER_PASSWORD')
        tasks_link = self.config.get('TASKS_SITE')

        self.browser.open(auth_link)
        self.browser.should_be(UrlExact(auth_link))
        auth_page = AuthPage(self.driver)
        log('Логинимся')
        auth_page.login_field.should_be(Visible)
        auth_page.login_field.type_in(login + Keys.ENTER).should_be(ExactText(login))
        auth_page.password_field.type_in(password + Keys.ENTER)
        delay(1)
        log('Переходим в раздел Задачи в работе')
        self.browser.open(tasks_link)
        tasks_page = TasksInWorkPage(self.driver)
        self.browser.should_be(TitleExact('Задачи на мне'))
        log('Выделена папка "Входящие" и стоит маркер')
        tasks_page.active_folder.should_be(ContainsText('Входящие'))
        tasks_page.active_folder.should_be(Present(tasks_page.marker))
        log('Убедиться, что папка не пустая')
        tasks_page.empty_folder.should_not_be(Visible)
        log('Переходим в другую папку, проверить что она выделена')
        tasks_page.folders.item(2).click()
        tasks_page.active_folder.should_not_be(ContainsText('Входящие'))
        tasks_page.active_folder.should_be(Present(tasks_page.marker))
        delay(1)
        log('Создаем новую папку')
        tasks_page.create_btn.click()
        tasks_page.folder_plus.click()
        tasks_page.input_name_folder.send_keys('Новая папка автотест')
        tasks_page.save_folder.click()
        log('Перейдем в новую папку и убедимся что пуста')
        tasks_page.folders.item(with_text='Новая папка автотест').click()
        tasks_page.empty_folder.should_be(Visible)
        log('Удалим новую папку')
        tasks_page.folders.item(with_text='Новая папка автотест').context_click()
        tasks_page.delete_btn.click()
        tasks_page.yes_delete.click()
        log('Проверим, что её нет в списке папок')
        tasks_page.folders.should_not_be(ContainsText('Новая папка автотест'))
