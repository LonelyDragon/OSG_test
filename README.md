### About
Реализация тестового фреймворка и тестов для [API](https://github.com/SergeyOlinichenko/test_ocs). Используется Page Object pattern.
### Progect stucture
Проект состоит:
./api/users - каталог с апи
./conftest.py - опции и фикстуры pytest
./test_api_get.py - кейсы для метода GET
./test_api_post.py - кейсы для метода POST
./test_api_delete.py - кейсы для метода DELETE
### Requirements
Python 3.7+
### Install
1. Склонировать репозиторий;
2. Создать виртуальное окружение и активировать его;
3. Установить зависимости:
`pip install -r requirements.txt`;
4. Запустить тесты с помощью pytest в следующем порядке: 
`test_api_get.py`;
`test_api_post.py`;
`test_api_delete.py`;