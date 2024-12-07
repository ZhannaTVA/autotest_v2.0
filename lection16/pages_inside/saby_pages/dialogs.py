from atf.ui import *
from atf import delay
from controls import *


class ContactsRegistry(Region):
    """Реестр Контакты"""

    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.msg-dialogs-folder .controls-Grid', 'Папки')
    dialogs = ControlsListView(By.CSS_SELECTOR, '.msg-dialogs-detail__list', 'Диалоги')
    chats = ControlsListView(By.CSS_SELECTOR, '.msg-CorrespondenceDetail', 'Чаты')
    correspondents = ControlsListView(By.CSS_SELECTOR, '.msg-people-actions .controls-ListViewV__itemsContainer', 'Контакты')
    mover_dialog = ControlsMoveDialog()
    tag_selector = ControlsListView(By.CSS_SELECTOR, '.controls-Popup .tags-list', 'Селектор тэгов')
    tag_tree_list = ControlsListView(By.CSS_SELECTOR, '.tags-list', 'Список тэгов')
    search = ControlsSearchInput()
    tabs = ControlsTabsButtons()

    def check_load(self):
        """Проверка загрузки реестра"""

        self.folders.check_load()
        self.dialogs.check_load()