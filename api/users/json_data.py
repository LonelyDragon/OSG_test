# todo: вынести сообщения в отдельный файл, чтобы можно было хранить схемы в json, а здесь сериализовать в объекты Python

class GetData:
    # валидная json схема для GET
    RESPONSE_USER_SCHEMA = {
        "type": "object",
        "required": ["data"],
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "type": "object",
                            "required": [
                                "id",
                                "first_name",
                                "second_name",
                                "age"
                            ],
                            "properties": {
                                "id": {"type": "integer"},
                                "first_name": {"type": "string"},
                                "second_name": {"type": "string"},
                                # отличие схем
                                "age": {"type": "integer"}
                            },
                            "additionalProperties": False
                        }
                    ]
                }
            }
        },
        "additionalProperties": False
    }


class PostData:
    # валидная user схема для POST
    RESPONSE_USER_SCHEMA = {
        "type": "object",
        "required": ["data"],
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "anyOf": [
                        {
                            "type": "object",
                            "required": [
                                "id",
                                "first_name",
                                "second_name",
                                "age"
                            ],
                            "properties": {
                                "id": {"type": "integer"},
                                "first_name": {"type": "string"},
                                "second_name": {"type": "string"},
                                # отличие схем
                                "age": {"type": "string"}
                            },
                            "additionalProperties": False
                        }
                    ]
                }
            }
        },
        "additionalProperties": False
    }
    # список валидных сообщений ошибок об отутствии обязательного поля
    ERROR_MSG = [
        {"message": {"age": "Missing required parameter in the JSON body or the post body or the query string"}},
        {"message": {"second_name": "Missing required parameter in the JSON body or the post body or the query string"}},
        {"message": {"first_name": "Missing required parameter in the JSON body or the post body or the query string"}},
    ]


class DeleteData:
    # сообщение об успешном удалении объекта
    SUCCESFUL_DELETE_MSG = {"message": "Record deleted successfully."}
    # сообщение об отсутствии обязательного поля
    ERROR_MSG = {"message": {
        "id": "Missing required parameter in the JSON body or the post body or the query string"}}
