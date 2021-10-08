from requests.models import Response
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from api.users.base import Base
from api.users.json_data import GetData
import requests


class Get(Base):

    # получение юзера по его id
    def get_user_by_id(self, id: int) -> Response:
        request = requests.get(f"{self.url}/users/{id}")
        assert request.status_code == 200, f"invalid HTTP code: {request.status_code}\nResponse: {request.json()}"
        return request

    # проверка возможности получения юзера, не передавая id
    def get_user_without_id(self) -> None:
        request = requests.get(f"{self.url}/users/")
        assert request.status_code != 404, f"should send response HTTP code: 404. HTTP code: {request.status_code}\nResponse: {request.json()}"

    # получение всех юзеров из бд
    def get_all_users(self) -> Response:
        request = requests.get(f"{self.url}/users")
        assert request.status_code == 200, f"invalid HTTP code: {request.status_code}"
        return request

    # осуществляет проверку JSON модели юзера приходящей в ответ на GET и POST
    def check_user_model_json_get(self, response: Response) -> None:
        data = response.json()
        try:
            validate(data, schema=GetData.RESPONSE_USER_SCHEMA)
        except ValidationError as err:
            raise err
