# Написать тесты по реестру Контакты (можно использовать свой реестр, если в нём существуют подобные проверки).
# 1. Переместить запись в другую папку и проверить перемещение
# (убедиться в: наличии в папке и увеличении счётчика). И вернуть обратно.
# 2. Проверить, что дата сообщения в реестре Диалоги совпадает с датой в Чатах
# 3. Пометить сообщение эталонным тегом.
# Убедиться, что тег появился на сообщении, а счётчик тегов увеличился.
# Снять тег и проверить.

from atf.ui import *
from atf import *
from atf.exceptions import *
from controls import *
from pages.auth_page import AuthPage
from pages.contacts_page import ContactsRegistry


class TestRegistryContact(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))
        cls.message = cls.config.get('MESSAGE_TEXT')
        cls.browser.open(cls.config.get('SITE_DIALOGS'))
        cls.page = ContactsRegistry(cls.driver)

    def setUp(self):
        self.browser.open(self.config.get('SITE_DIALOGS'))
        self.page.check_load()

    def test_01_move_message(self):
        """Перемещение сообщения в папку и обратно"""

        move_folder = self.config.get('FOLDER_NAME')
        main_folder = self.config.get('FOLDER_ALL')
        action = 'Перенести в папку'

        log('Перемещаем сообщение в заданную папку')
        self.page.dialogs.item(contains_text=self.message).select_menu_actions(action)
        self.page.mover_dialog.select(contains_text=move_folder)
        log('Проверяем, что сообщение переместилось в папку и увеличился счетчик')
        self.page.folders.row(contains_text=move_folder).click()
        self.page.dialogs.item(contains_text=self.message).should_be(Displayed)
        self.page.dialogs.check_size(1)
        log('Перемещаем сообщение обратно')
        self.page.dialogs.item(contains_text=self.message).select_menu_actions(action)
        self.page.mover_dialog.move_root()
        self.page.dialogs.item(contains_text=self.message).should_not_be(Displayed)
        self.page.folders.row(contains_text=main_folder).click()
        self.page.dialogs.item(contains_text=self.message).should_be(Displayed)

    def test_02_compare_date(self):
        """Проверка даты сообщения"""

        recepient = self.config.get('MSG_RECEPIENT')

        log('Проверяем дату сообщения в диалогах')
        dialog_date = self.page.dialogs.item(contains_text=self.message).element('[data-qa="msg-entity-date"]').text

        log('Проверяем дату сообщения в чатах')
        self.page.tabs.select('Чаты')
        self.page.correspondents.element(f'[title="{recepient}"]').click()
        self.page.chats.item(contains_text=self.message).should_be(ContainsText(dialog_date))

    def test_03_tags(self):
        """Проверка работы тегов"""

        tag = self.config.get('TAG')
        action = 'Пометить'

        log('Помечаем сообщение тэгом')
        self.page.dialogs.item(contains_text=self.message).select_menu_actions(action)
        self.page.tag_selector.item(contains_text=tag).click()

        log('Убедиться, что тег появился на сообщении, а счётчик тегов увеличился')
        self.page.dialogs.item(contains_text=self.message).should_be(ContainsText(tag))
        self.page.tag_tree_list.item(contains_text=tag).click()
        self.page.dialogs.item(contains_text=self.message).should_be(Displayed)
        self.page.dialogs.check_size(1)

        log('Снять тег и проверить')
        self.page.dialogs.item(contains_text=self.message).select_menu_actions('Пометить')
        self.page.tag_selector.item(contains_text=tag).click()
        self.page.dialogs.item(contains_text=self.message).should_not_be(Displayed)
        self.page.search.send_keys(Keys.BACK_SPACE)
        self.page.dialogs.item(contains_text=self.message).should_be(Displayed)
