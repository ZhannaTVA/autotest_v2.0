from atf.ui import *
from atf import *


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[type="text"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '[type="password"]', 'пароль')

    def auth(self, login: str, password: str):
        """
        Авторизация на онлайне
        :param login: Логин
        :param password: Пароль
        """
        self.browser.open(self.config.get('SITE'))
        self.login.type_in(login + Keys.ENTER)
        self.login.should_be(ExactText(login))
        self.password.type_in(password + Keys.ENTER)
