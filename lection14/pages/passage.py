from controls import *
from atf.ui import *


@templatename("EDO3/passage:Panel")
class Panel(DialogTemplate):
    """Панель выбора сотрудника"""

    staff_cl = ControlsLookupInput(SabyBy.DATA_QA, 'staffCommon-Lookup', 'Согласующий')
    approve_el = Element(By.CSS_SELECTOR, '[data-qa="edo3-PassageList__action-button"]',
                              'На согласование')

    def select_staff(self, staff: str):
        """Выбрать сотрудника
        :param staff: ФИО выбираемого сотрудника
        """

        self.staff_cl.autocomplete_search(staff)
        self.approve_el.click()
