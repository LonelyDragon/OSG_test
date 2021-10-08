import csv


class Base:
    def __init__(self, url: str) -> None:
        self.url = url


# реализовал класс подключения и управления бд, но не стал подключать в работу
class DB:
    def __init__(self, path: str) -> None:
        self.path = path

    # реализовал метод для проверки нахождения json модели юзера в csv.
    def check_user_in_the_db(self, user: dict) -> None:
        data = csv.DictReader(open("./users.csv"))
        user = {k: str(v) for k, v in user["data"][0].items()}
        for row in data:
            if user == row:
                break
            else:
                raise ValueError(f"User data does not exist in csv {user}")

    # реализация метода для проверки отсутствия записи в бд
    def check_user_is_not_in_the_db(self, user: dict) -> None:
        data = csv.DictReader(open("./users.csv"))
        user = {k: str(v) for k, v in user["data"][0].items()}
        for row in data:
            if user == row:
                raise ValueError(f"User data exist in csv {user}")
