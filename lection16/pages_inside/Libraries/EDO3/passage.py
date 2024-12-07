from controls import *
from atf.ui import *


@templatename("EDO3/passage:Panel")
class Panel(DialogTemplate):
    """Панель выбора сотрудника"""

    staff_cl = ControlsLookupInput(SabyBy.DATA_QA, 'staffCommon-Lookup', 'Согласующий')
    approve_el = Element(By.CSS_SELECTOR, '[title="Согласовать отгул"] .controls-BaseButton__text',
                              'Согласовать отгул')

    def select_staff(self, staff):
        """Выбрать сотрудника для согласования отгула"""

        self.staff_cl.autocomplete_search(staff)
        self.approve_el.click()