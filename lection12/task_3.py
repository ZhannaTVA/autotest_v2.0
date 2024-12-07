# Авторизоваться на сайте https://fix-online.sbis.ru/
# Откройте эталонную задачу по прямой ссылке в новом окне
# Убедитесь, что в заголовке вкладки отображается "Задача № НОМЕР от ДАТА",где ДАТА и НОМЕР - это
# ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными
# значениями

from atf.ui import *
from atf import log, info, delay


class AuthPage(Region):
    login_field = TextField(By.CSS_SELECTOR, '[type="text"]', 'Логин')
    password_field = TextField(By.CSS_SELECTOR, '[type="password"]', 'Пароль')


class TaskPage(Region):
    executor = Element(By.CSS_SELECTOR, '.edws-StaffChooser__itemTpl-name', 'Исполнитель ')
    data = Element(By.CSS_SELECTOR, '[data-qa="edo3-Document_docDate"]', 'Дата')
    number = Element(By.CSS_SELECTOR, '[data-qa="edo3-Document_docNumber"]', 'Номер')
    description = Element(By.CSS_SELECTOR, ".richEditor_Base_textContainer p", 'Описание')
    author = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]', 'Автор')


class Test(TestCaseUI):

    def test(self):
        auth_link = self.config.get('AUTH_SITE')
        login = self.config.get('USER_LOGIN')
        password = self.config.get('USER_PASSWORD')
        task = self.config.get('TASK_LINK')
        task_title = self.config.get('TASK_TITLE')
        task_executor = self.config.get('TASK_EXECUTOR')
        task_data = self.config.get('TASK_DATA')
        task_number = self.config.get('TASK_NUMBER')
        task_description = self.config.get('TASK_DESCRIPTION')
        task_author = self.config.get('TASK_AUTHOR')

        self.browser.open(auth_link)
        self.browser.should_be(UrlExact(auth_link))
        auth_page = AuthPage(self.driver)
        log('Логинимся')
        auth_page.login_field.should_be(Visible)
        auth_page.login_field.type_in(login + Keys.ENTER).should_be(ExactText(login))
        auth_page.password_field.type_in(password + Keys.ENTER)
        delay(1)
        log('Откройте эталонную задачу по прямой ссылке в новом окне')
        open_task = lambda: self.browser.create_new_tab(task)
        self.browser.switch_to_opened_window(open_task)
        task_page = TaskPage(self.driver)
        log('Убедитесь, что в заголовке вкладки отображается эталонный "Задача № НОМЕР от ДАТА"')
        self.browser.should_be(TitleExact(task_title))
        log('Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями')
        task_page.executor.should_be(ExactText(task_executor))
        task_page.data.should_be(ExactText(task_data))
        task_page.number.should_be(ExactText(task_number))
        task_page.description.should_be(ExactText(task_description))
        task_page.author.should_be(ExactText(task_author))
