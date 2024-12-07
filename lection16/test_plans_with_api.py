from atf import *
from atf.ui import *
from datetime import *
from pages_inside.auth_online import AuthOnline
from pages_inside.saby_pages.plans import Plans
from pages_inside.Libraries.EDOPlans.dialog import Dialogs


class TestCreatePlan(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthOnline(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

    def setUp(self):
        Plans(self.driver).open()

    def test_create_plan(self):
        """
        Создайте план работ
        Выберите объект планирования через панель выбора.
        Укажите заказчика
        Добавьте пункт плана, указав описание и исполнителя
        Запустите план в документооборот
        Откройте созданный план и убедитесь, что пункт плана, заказчик и исполнитель
        отображаются согласно введенным ранее данным
        Удалите созданный план через реестр
        Убедитесь, что план не отображается в реестре.
        """
        plans_page = Plans(self.driver)
        log('Создаем план')
        log('Создаем план')
        plan_card = plans_page.create_plan(('План работ',))
        log('Заполняем карточку плана')
        plan_data = {"Объект планирования": self.config.get('PLANNING_OBJ'), "Заказчик": self.config.get('CUSTOMER')}
        log('Выбираем объект планирования и заказчика')
        plan_card.fill_plan(**plan_data)
        log('Создаем и заполняем пункт плана')
        point_data = {"Тип пункта": self.config.get('POINT_TYPE'), "Описание": self.config.get('POINT_DESC'),
                      "Исполнитель": self.config.get('POINT_EXECUTOR'), "Принимающий": self.config.get('POINT_CUSTOMER')}
        plan_card.add_plan_point(**point_data)
        log('Запускаем план в работу')
        plan_card.run_plan()
        log('Открываем план из реестра')
        plans_page.open_plan()
        log('Проверка полей плана и пункта плана')
        plan_card.check_plan_field(plan_data, point_data)
        log('Удаление плана через реестр')
        plans_page.delete_plan(**plan_data)