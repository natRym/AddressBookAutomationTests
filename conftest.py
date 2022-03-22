import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseURL = request.config.getoption("--baseURL")
    admin_password = request.config.getoption("--admin_password")
    if fixture is None:
        fixture = Application(browser=browser, baseURL=baseURL)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password=admin_password)
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finalizer():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(finalizer)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")
    parser.addoption("--admin_password", action="store", default="secret")
