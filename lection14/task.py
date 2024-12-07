from atf import *
from atf.ui import *
from datetime import *
from pages.AuthPages import AuthPage
from pages.WorkScheduleDocuments import WorkScheduleDocuments


def get_tomorrow_date():
    return date.today() + timedelta(days=1)


class TestCreateTimeOff(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

    def setUp(self):
        WorkScheduleDocuments(self.driver).open()

    def test_timeoff_without_time(self):
        """
        Создать отгул
        Выбрать сотрудника через автодополнение, которому создаем отгул
        Выставить дату - завтра
        Заполнить причину
        Запустить в ДО
        Убедиться, что появился в реестре и при переоткрытии значения в полях сохранились
        Удалить отгул
        """
        timeoff_data = {'Сотрудник': self.config.get("EMPLOYEE"), 'Причина': self.config.get("REASON1"),
                        'Дата': get_tomorrow_date()}
        timeoff_page = WorkScheduleDocuments(self.driver)
        log('Создаем отгул')
        timeoff_card = timeoff_page.create_document(('Отгул', 'Отгул'))
        log('Заполнение карточки отгула')
        timeoff_card.fill_timeoff(**timeoff_data)
        timeoff_card.run_timeoff(self.config.get('STAFF'))
        timeoff_page.open_document(**timeoff_data)
        timeoff_card.check_fields(**timeoff_data)
        timeoff_card.delete_card()
        timeoff_page.check_delete_document(**timeoff_data)

    def test_timeoff_with_time(self):
        """
        Создать отгул
        Выбрать сотрудника через справочник
        Выставить время завтра с 12 до 14 часов
        Заполнить описание
        Сохранить
        Убедиться, что появился в реестре и при переоткрытии значения в полях сохранились
        Удалить отгул
        """
        timeoff_data = {'Сотрудник': self.config.get("EMPLOYEE"), 'Причина': self.config.get("REASON2"),
                        'Дата': get_tomorrow_date(), 'Со скольки': self.config.get('TIME_FROM'),
                        'До скольки': self.config.get('TIME_TO')}
        timeoff_page = WorkScheduleDocuments(self.driver)
        log('Создаем отгул')
        timeoff_card = timeoff_page.create_document(('Отгул', 'Отгул'))
        log('Заполнение карточки отгула')
        timeoff_card.fill_timeoff(**timeoff_data, autocomplete=False)
        timeoff_card.run_timeoff(self.config.get('STAFF'))
        timeoff_page.open_document(**timeoff_data)
        timeoff_card.check_fields(**timeoff_data)
        timeoff_card.delete_card()
        timeoff_page.check_delete_document(**timeoff_data)