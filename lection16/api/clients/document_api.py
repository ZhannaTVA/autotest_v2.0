from atf.api.base_api_ui import BaseApiUI


class Document(BaseApiUI):
    """API методы объекта Документ"""

    def delete(self, ids):
        """
        Удалить документ по ID
        :param ids: ID документа
        """
        params = {'ИдО': ids}

        return self.client.call_rvalue(method='Документ.УдалитьДокументы', **params).result