from controls import *
from atf.ui import *


@templatename("WorkTimeDocuments/timeoff:Dialog")
class Dialog(DocumentTemplate):
    """Карточка отгула"""

    employee_cl = ControlsLookupInput(SabyBy.DATA_QA, 'staff-Lookup__input', 'Сотрудник')
    reason_re = RichEditorExtendedEditor(SabyBy.DATA_QA, 'wtd-Base__comment', 'Причина')
    date_elm = Element(By.CSS_SELECTOR, '.wtd-dayTimeSelector--hover-cursor-pointer', 'Дата')
    date_txt = Element(By.CSS_SELECTOR, '[data-qa="wtd-DayTimeSelector__dateInput"]', 'Дата отгула')
    phase_el = Element(By.CSS_SELECTOR, '.edo3-PassageButton__button', 'На выполнение')
    delete_btn_elm = Element(SabyBy.DATA_QA, 'deleteDocument', 'Удалить отгул')
    calendar_pd = ControlsDatePopup(By.CSS_SELECTOR, '[data-qa="controls-PeriodDialog"]', 'Календарь')
    time_from_elm = ControlsInputMask(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__start', 'Со скольки')
    time_to_elm = ControlsInputMask(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__end', 'До скольки')
    time_elm = Button(By.CSS_SELECTOR, '[title="Указать часы отгула"] span', 'Время отгула')

    def fill_timeoff(self, autocomplete=True, **kwargs):
        """Заполнять задачу"""

        if 'Сотрудник' in kwargs.keys():
            if autocomplete:
                self.employee_cl.autocomplete_search(kwargs['Сотрудник'])
            else:
                self.employee_cl.select_from_catalog(kwargs['Сотрудник'])
        if 'Причина' in kwargs.keys():
            self.reason_re.type_in(kwargs['Причина'])
        if 'Дата' in kwargs.keys():
            self.date_elm.click()
            self.calendar_pd.select_period(kwargs['Дата'])
        if 'Со скольки' in kwargs.keys() and 'До скольки' in kwargs.keys():
            self.time_elm.click()
            self.time_from_elm.type_in(kwargs['Со скольки'])
            self.time_to_elm.type_in(kwargs['До скольки'])


    def run_timeoff(self, staff):
        """Отправить на согласование"""

        from pages_inside.Libraries.EDO3.passage import Panel

        self.phase_el.click()
        agreement = Panel(self.driver)
        agreement.select_staff(staff)
        agreement.check_close()
        self.check_close()

    def check_fields(self, **kwargs):
        """Проверка полей документа"""

        if 'Сотрудник' in kwargs.keys():
            self.employee_cl.should_be(ContainsText(kwargs['Сотрудник']))
        if 'Причина' in kwargs.keys():
            self.reason_re.should_be(ContainsText(kwargs['Причина']))
        if 'Дата' in kwargs.keys():
            self.date_txt.should_be(ContainsText(kwargs['Дата'].strftime('%d.%m.%y')))

    def close_card(self):
        """Закрыть карточку"""
        self.close_btn.click()
        self.check_close()

    def delete_card(self):
        """Удалить карточку"""
        self.delete_btn_elm.click().send_keys(Keys.ENTER)
        self.check_close()