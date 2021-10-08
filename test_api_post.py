from api.users.post import Post
import pytest

'''
POST /users - создает новую запись в users.csv, обязательные поля в json: first_name - имя пользователя 
last_name - фамилия пользователя age - возраст пользователя
'''

class TestPositiveCase:
    test_data_json = [
        {
            "first_name":"Ivan",
            "second_name":"Ivanovich",
            "age":17
        },
        {
            "first_name":"Иван",
            "second_name":"Иванович",
            "age":33
        }
    ]
    # проверка создания пользователя с отправкой валидного json body
    @pytest.mark.parametrize("vars_json", test_data_json)
    def test_create_user(self, api_url, vars_json):
        api = Post(api_url)
        api.create_user(vars_json)

    # проверка валидного ответа при создании пользователя
    @pytest.mark.parametrize("vars_json", test_data_json)
    def test_json_create_user(self, api_url, vars_json):
        api = Post(api_url)
        data = api.create_user(vars_json)
        api.check_user_model_json_post(data)

class TestNegativeCase:
    test_data_json = [
        {
            "first_name":"Ivan",
            "second_name":"Ivanovich"
        },
        {
            "first_name":"Ivan",
            "age": 55
        },
        {
            "second_name":"Ivanovich",
            "age": 44
        }
    ]

    test_data_json_invalid = [
        {
            "first_name":"Иван",
            "second_name":55,
            "age":"test"
        },
        {
            "first_name":55,
            "second_name":"Ivan",
            "age":"test"
        },
        {
            "first_name":55.0,
            "second_name":"Ivanovich",
            "age": 440000000000000000000
        }
    ]
    # проверка валидного ответа при отправке невалидного body на создания пользователя
    @pytest.mark.parametrize("vars_json", test_data_json)
    def test_create_user_error_message(self, api_url,vars_json):
        api = Post(api_url)
        responce = api.create_user(vars_json)
        api.check_error_requered_fields(responce)
    # проверка создания пользователя с отправкой невалидных типов json body
    @pytest.mark.parametrize("vars_json", test_data_json_invalid)
    def test_create_user_n(self, api_url, vars_json):
        api = Post(api_url)
        api.create_user(vars_json)