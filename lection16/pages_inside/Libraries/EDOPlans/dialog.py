from controls import *
from atf.ui import *
from atf import delay
from lection16.pages_inside.Libraries.EDOPlans.point import Dialog


@templatename("EDOPlans/dialog:Dialog")
class Dialogs(DocumentTemplate):
    """Карточка плана"""

    planning_obj_cl = ControlsLookupInput(SabyBy.DATA_QA, 'PlanCard_Main', 'Объект планирования')
    customer_elm = ControlsLookupSelector(SabyBy.DATA_QA, 'edo3-Sticker__mainInfo', 'Укажите заказчика')
    plan_menu_cm = ControlsMenuControl(SabyBy.DATA_QA, 'cell', 'Меню пунктов плана')
    phase_db = ControlsButton(By.CSS_SELECTOR, '[data-qa="extControls-doubleButton__caption"]', 'На выполнение')
    points_list_tgv = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="list"].planItems-list__bottom', 'Пункты плана')

    def fill_plan(self, **kwargs):
        """заполнение карточки плана
        :param **kwargs данные плана Объект планирования и Заказчик"""
        if 'Объект планирования' in kwargs.keys():
            self.planning_obj_cl.select_from_catalog(kwargs['Объект планирования'])
        if 'Заказчик' in kwargs.keys():
            delay(1.5)
            self.customer_elm.select_from_catalog(kwargs['Заказчик'])
            delay(0.5)

    def add_plan_point(self, **kwargs):
        """Добавление пункта плана
        :param **kwargs данные пункта плана"""
        self.plan_menu_cm.select(kwargs['Тип пункта'])
        point_card = Dialog(self.driver)
        point_card.check_open()
        point_card.fill_plan_point(**kwargs)
        point_card.save_point()

    def run_plan(self):
        """Запуск плана"""
        self.phase_db.click()
        self.check_close()

    def check_plan_field(self, plan_data: dict, point_data: dict):
        """Проверка полей плана и пункта плана
        :param plan_data: dict данные полей плана
        point_data: dict данные полей пункта плана"""
        if 'Объект планирования' in plan_data.keys():
            self.planning_obj_cl.should_be(ContainsText(plan_data['Объект планирования']))
        if 'Заказчик' in plan_data.keys():
            custom_strform = f'{plan_data["Заказчик"][:plan_data["Заказчик"].find(" ")+2]}.'
            self.customer_elm.should_be(ExactText(custom_strform))
        self.points_list_tgv.cell(contains_text=point_data['Описание']).click()
        Dialog(self.driver).check_point_field(point_data)
        self.close()
