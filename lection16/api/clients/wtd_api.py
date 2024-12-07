from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *
from datetime import datetime
from datetime import *


class WTD(BaseApiUI):
    """API методы объекта WTD"""

    def list(self, search):
        """
        Поиск по документам.
        :param search: строка для поиска.
        :return: результат поиска - список документов
        """
        start_date = date.today() + timedelta(days=1)
        end_date = date.today() + timedelta(days=1)

        params = generate_record_list(ФильтрДатаПериод='Период', ТипДокумента='Отгул', ФильтрМоиДокументы='Все',
                                      ФильтрПоиска=search, ФильтрДатаС=str(start_date), ФильтрДатаП=str(end_date))

        return self.client.call_rrecordset(method='WTD.List', **params).result