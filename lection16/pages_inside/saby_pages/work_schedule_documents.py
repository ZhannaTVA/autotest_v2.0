from atf import *
from atf.ui import *
from controls import *
from lection16.pages_inside.Libraries.WorkTimeDocuments.timeoff import Dialog


class WorkScheduleDocuments(Region):
    """Реестр документов графика работ"""

    create_timeoff = ExtControlsDropdownAddButton()
    doc_list_tgv = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MasterDetail_detailsContent .controls-Grid',
                                        'Список документов')
    timeoff_list_cslst = ControlsTreeGridView(By.CSS_SELECTOR, '.wtd-DocumentTypes__scroll .controls-Grid',
                                        'Типы документов')
    search_cit = ControlsInputText(By.CSS_SELECTOR, '[data-qa="wtd-Registry_search"]', 'Поиск')

    def open(self):
        """Переходим в реестр График работ/документы"""
        self.browser.open(self.config.get('SHEDULE_PAGE'))
        self.check_page_load_wasaby()

    def create_document(self, regulation: tuple):
        """
        Создание отгула.
        :param regulation: путь до создаваемого документа
        """

        self.create_timeoff.select(*regulation)
        timeoff_card = Dialog(self.driver)
        timeoff_card.check_open()
        return timeoff_card

    def open_document(self, **kwargs):
        """Проверка наличия отгула в реестре. Открытие карточки"""

        self.search_cit.type_in(kwargs['Сотрудник'])
        self.doc_list_tgv.cell(contains_text=kwargs['Причина']).should_be(Displayed)
        self.doc_list_tgv.cell(contains_text=kwargs['Причина']).click()

    def check_delete_document(self, **kwargs):
        """Проверка отсутствия удаленного документа в реестре"""
        self.search_cit.type_in(kwargs['Сотрудник'])
        self.doc_list_tgv.cell(contains_text=kwargs['Причина']).should_not_be(Displayed)

    def delete_document(self, text):
        self.timeoff_lst.row(contains_text=text).select_menu_actions('Удалить')
        self.popup_confirmation.confirm()
        