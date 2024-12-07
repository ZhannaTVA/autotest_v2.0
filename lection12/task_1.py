# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import log, info, delay


class AuthPage(Region):
    login_field = TextField(By.CSS_SELECTOR, '[type="text"]', 'Логин')
    password_field = TextField(By.CSS_SELECTOR, '[type="password"]', 'Пароль')


class ContactsPage(Region):
    plus_btn = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]', 'Кнопка +')
    search_input = TextField(By.CSS_SELECTOR, '[class="controls-StackTemplate-content"] [inputmode="text"]', 'Строка поиска')
    recipient = Element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]', 'Карточка сотрудника')
    input_message = Element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]', 'Поле ввода сообщения')
    send_btn = Button(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]', 'Отправить')
    messages = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p', 'Список сообщений')
    delete_btn = Button(By.CSS_SELECTOR, '[title="Перенести в удаленные"]', 'Удалить')


class Test(TestCaseUI):

    def test(self):
        auth_link = self.config.get('AUTH_SITE')
        login = self.config.get('USER_LOGIN')
        password = self.config.get('USER_PASSWORD')
        contacts_link = self.config.get('CONTACTS_SITE')
        recipient_name = self.config.get('RECIPIENT_NAME')
        message_text = self.config.get('MESSAGE_TEXT')

        self.browser.open(auth_link)
        self.browser.should_be(UrlExact(auth_link))
        auth_page = AuthPage(self.driver)
        log('Логинимся')
        auth_page.login_field.should_be(Visible)
        auth_page.login_field.type_in(login + Keys.ENTER).should_be(ExactText(login))
        auth_page.password_field.type_in(password + Keys.ENTER)
        delay(1)
        log('Переходим в раздел Контакты')
        self.browser.open(contacts_link)
        contacts_page = ContactsPage(self.driver)
        log('Отправляем сообщение самому себе')
        contacts_page.plus_btn.click()
        contacts_page.search_input.click().type_in(recipient_name)
        contacts_page.recipient.should_be(Attribute(title=recipient_name)).click()
        contacts_page.input_message.click().type_in(message_text)
        contacts_page.send_btn.click()
        log('Убедиться, что сообщение появилось в реестре')
        contacts_page.messages.item(1).should_be(ExactText(message_text))
        contacts_page.messages.mouse_over()
        log('Удалим сообщение')
        contacts_page.delete_btn.click()
        log('Убедиться, что удалили сообщение')
        contacts_page.messages.item(1).should_not_be(ExactText(message_text))
