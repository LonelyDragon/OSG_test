import pytest


def pytest_addoption(parser) -> None:
    parser.addoption('--url', action='store', default='127.0.0.1',
                     help="url api. Default: 127.0.0.1")
    parser.addoption('--port', action='store', default='5000',
                     help="port. Default: 5000")
    parser.addoption('--bd', action='store', default="./users.csv",
                     help="bd path. Default: ./users.csv")


@pytest.fixture(scope="function", autouse=True)
def api_url(request) -> str:
    url = request.config.getoption("url")
    port = request.config.getoption("port")
    return f"http://{url}:{port}"


@pytest.fixture(scope="function")
def bd_path(request) -> str:
    return request.config.getoption("bd")
