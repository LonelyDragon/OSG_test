from api.users.get import Get
import pytest
'''
GET /users - возвращает всех пользователей из users.csv
GET /users/{userid} - возвращает данные пользователя с id = userid
'''


class TestPositiveCase:
    test_var = [
        1,2,3
    ]
    # проверка метода на получение юзера параметром строки
    @pytest.mark.parametrize("vars", test_var)
    def test_get_user_by_id(self, api_url, vars):
        api = Get(api_url)
        api.get_user_by_id(vars)

    # проверка валидности ответа json body в соответствии со схемой user (id, first_name, second_name, age)
    def test_json_get_user_by_id(self, api_url):
        api = Get(api_url)
        data = api.get_user_by_id(2)
        api.check_user_model_json_get(data)

    # проверка метода на получение всех пользователей из базы
    def test_get_all_users(self, api_url):
        api = Get(api_url)
        api.get_all_users()

    # проверка валидности на получение всех пользователей ответа json body 
    # в соответствии со схемой user (id, first_name, second_name, age)
    def test_json_get_all_users(self, api_url):
        api = Get(api_url)
        data = api.get_all_users()
        api.check_user_model_json_get(data)

class TestNegativeCase:

    test_var = [
        -1,2.0,9990, "test"
    ]
    @pytest.mark.parametrize("vars", test_var)
    def test_get_user_by_id(self, api_url, vars):
        api = Get(api_url)
        api.get_user_by_id(vars)