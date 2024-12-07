from controls import *
from atf.ui import *


@templatename("EDOPlans/point:Dialog")
class Dialog(StackTemplate):
    """Пункт плана"""

    description_cia = ControlsInputArea()
    description_txt = Element(By.CSS_SELECTOR, '.controls-Area__wrapURLs', 'Текст поля Перечень работ')
    customer_ls = ControlsLookupSelector(SabyBy.DATA_QA, 'SelectedCollection__item', 'Принимающий')
    add_executors_cslst = ControlsLookupSelector(By.CSS_SELECTOR, '.plan-PointImplementers__addBtn', '+Исполнители')
    save_db = ControlsButton(By.CSS_SELECTOR, '.edo3-ReadOnlyStateButton__container', 'Сохранить')
    executors_list = ControlsTreeGridView(By.CSS_SELECTOR, '.plan-PointImplementers', 'Список исполнителей')

    def fill_plan_point(self, **kwargs):
        """Заполняем пункт плана"""
        if 'Описание' in kwargs.keys():
            self.description_cia.type_in(kwargs['Описание'])
        if 'Принимающий' in kwargs.keys():
            self.customer_ls.select_from_catalog(kwargs['Принимающий'])
        if 'Исполнитель' in kwargs.keys():
            self.add_executors_cslst.select_from_catalog(kwargs['Исполнитель'])

    def save_point(self):
        """Сохранение пункта плана"""
        self.save_db.click()

    def check_point_field(self, point_data: dict):
        """Проверка полей плана и пункта плана
        :param point_data: dict данные полей пункта плана"""
        if 'Описание' in point_data.keys():
            self.description_txt.should_be(ExactText(point_data['Описание']))
        if 'Принимающий' in point_data.keys():
            custom_strform = f'{point_data["Принимающий"][:point_data["Принимающий"].find(" ") + 2]}.'
            self.customer_ls.should_be(ExactText(custom_strform))
        if 'Исполнитель' in point_data.keys():
            self.executors_list.row(contains_text=point_data['Исполнитель']).should_be(Displayed)
        self.close()