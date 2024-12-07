from atf import *
from atf.ui import *
from controls import *
from lection15.pages_inside.Libraries.EDOPlans.dialog import Dialogs


class Plans(Region):
    """Реестр планов"""

    cteate_plan_ab = ExtControlsDropdownAddButton()
    plans_list_tgv = ControlsTreeGridView(By.CSS_SELECTOR, '.plan-List__masterView .controls-Grid', 'Дерево планов')
    list_of_plan = ControlsTreeGridView(By.CSS_SELECTOR, '.plan-List__detailsView', 'Список планов')

    def open(self):
        """Переходим в реестр Планы"""
        self.browser.open(self.config.get('PLANS_PAGE'))
        self.check_page_load_wasaby()

    def create_plan(self, regulation: tuple):
        """Создание карточки плана
        :param regulation - путь до создаваемого документа"""
        self.plans_list_tgv.row(contains_text='Все').click()
        self.cteate_plan_ab.select(*regulation)
        plan_card = Dialogs(self.driver)
        plan_card.check_open()
        return plan_card

    def open_plan(self):
        self.plans_list_tgv.row(contains_text=self.config.get('PLANNING_OBJ')).click()
        delay(0.5)
        self.list_of_plan.cell(contains_text=self.config.get('POINT_DESC')).click()

    def delete_plan(self, **kwargs):
        """Удаление плана через реестр
        :param **kwargs - данные плана, который удаляем"""
        self.plans_list_tgv.row(contains_text=self.config.get('PLANNING_OBJ')).click()
        delay(0.5)
        plan_for_delete = self.list_of_plan.item(contains_text=self.config.get('POINT_DESC'))
        plan_for_delete.delete(menu=True)
        self.popup_confirmation.confirm()
        self.list_of_plan.item(contains_text=self.config.get('POINT_DESC')).should_not_be(Displayed)
