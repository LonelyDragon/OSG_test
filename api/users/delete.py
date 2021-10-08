from requests.models import Response
from api.users.base import Base
from api.users.json_data import DeleteData
import requests


class Delete(Base):

    # метод для удаления юзера с body
    def delete_user_id_json(self, body: dict) -> Response:
        request = requests.delete(f"{self.url}/users", json=body)
        if request.status_code in (200, 400, 500):
            assert request.status_code in (
                200, 400), f"User is not deleted: {request.status_code}\n{request.json()}"
            return request

    # метод для удаления юзера через параметр запроса
    def delete_user_id_with_param(self, id: int) -> Response:
        request = requests.delete(f"{self.url}/users/{id}")
        assert request.status_code == 200, f"User is not deleted.\n{request.json()}"
        return request

    # проверка body на сообщение об успешном удалении
    def check_json_successful_delete(self, message: Response) -> None:
        assert message.json(
        ) == DeleteData.SUCCESFUL_DELETE_MSG, f"Response message doesn't match: {message}"

    # проверка body на сообщение об отсутствии обязательного параметра в json для удаления user
    def check_unseccessfull_delete_msg(self, message: Response) -> None:
        assert message.json(
        ) == DeleteData.ERROR_MSG, f"Response error message doesn't match: {message.json()}"
