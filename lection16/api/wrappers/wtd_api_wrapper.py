from atf.api.base_api_ui import BaseApiUI
from lection16.api.clients.document_api import Document
from lection16.api.clients.wtd_api import WTD
from atf import *


class WTDFunctions(BaseApiUI):
    """Методы для работы с документом Отгула"""

    def delete_document(self, search: str):
        """
        Удалить отгул.
        :param search: Строка для поиска отгула.
        """

        assert_that(search, not_equal(''), 'Передана пустая строка для поиска')

        wtd = WTD(self.client).list(search)
        document = Document(self.client)

        for doc in wtd:
            if doc['EmployeeFIOList'] == search:
                document.delete(doc['DocID'])

        assert_that(WTD(self.client).list(search), equal_to([]), 'Отгул не был удален')