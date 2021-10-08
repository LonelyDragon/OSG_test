from requests.models import Response
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from api.users.base import Base
from api.users.json_data import PostData
import requests


class Post(Base):

    # метод создания юзера
    def create_user(self, body: dict) -> Response:
        request = requests.post(f"{self.url}/users", json=body)
        if request.status_code in (201, 400):
            assert request.status_code in (
                201, 400), f"Request failed. User was not created or undefined error: {request.status_code}\n{request.json()}"
            return request

    # метод для проверки валидных сообщений об ошибке
    def check_error_requered_fields(self, body: Response) -> None:
        error = body.json()
        assert error in PostData.ERROR_MSG, f"Response error message doesn't match: {error}"

    def check_user_model_json_post(self, response: Response) -> None:
        data = response.json()
        try:
            validate(data, schema=PostData.RESPONSE_USER_SCHEMA)
        except ValidationError as err:
            raise err
