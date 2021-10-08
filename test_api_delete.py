from api.users.delete import Delete
import pytest
'''
DELETE /users - принимает json с значением id и удаляет запись с этим id
DELETE /users/userid - удаляет запись с id = userid
'''

class TestPositiveCase:
    test_data = [
        1, 2, 3, 4
    ]
    # проверка успешного удаления пользователя с отправкой валидного json body
    def test_delete_user_from_json(self, api_url):
        api = Delete(api_url)
        api.delete_user_id_json(5)

    # проверка удаления пользователя по id с отправкой валидного идентификатора через параметр строки (параметризировать)
    @pytest.mark.parametrize("vars", test_data)
    def test_delete_user_from_url_p(self, api_url, vars):
        api = Delete(api_url)
        api.delete_user_id_with_param(vars)
    
    # проверка сообщения об успешном удалении пользователя по id с отправкой параметра строки (параметризировать)
    @pytest.mark.parametrize("vars", test_data)
    def test_delete_message_user_from_url(self, api_url, vars):
        api = Delete(api_url)
        data = api.delete_user_id_with_param(vars)
        api.check_json_successful_delete(data)

    # проверка сообщения об успешном удалении пользователя c отправкой валидного json body
    #@pytest.mark.parametrize("vars", test_data)
    def test_json_delete_user_from_json(self, api_url):
        api = Delete(api_url)
        body = api.delete_user_id_json({"id": 5})
        api.check_json_successful_delete(body)

class TestNegativeCase:
    test_data = [
        -1, "test", 1.0, 999
    ]
    test_data_json = [
        {"id":""},
        {"id":"test"},
        {"id":88888},
        {"id":1.0},
        {"id":-1}
    ]
    # проверка сообщения об удалении пользователя по id с отправкой невалидного параметра строки
    @pytest.mark.parametrize("vars", test_data)
    def test_delete_user_from_url(self, api_url, vars):
        api = Delete(api_url)
        body = api.delete_user_id_with_param(vars)
        api.check_json_successful_delete(body)

    # проверка сообщения об удалении пользователя по id с отправкой невалидного json body
    @pytest.mark.parametrize("vars_json", test_data_json)
    def test_delete_user_from_json_n(self, api_url, vars_json):
        api = Delete(api_url)
        body = api.delete_user_id_json(vars_json)
        api.check_json_successful_delete(body)

    # проверка сообщения об отсутствии обязательного параметра id
    def test_delete_user_message_from_json_n(self, api_url):
        api = Delete(api_url)
        body = api.delete_user_id_json({"test": "test"})
        api.check_unseccessfull_delete_msg(body)