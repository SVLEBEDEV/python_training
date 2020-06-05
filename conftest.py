import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.application import Application
from fixture.db import DBficture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseURL=web_config['baseURL'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixtute = DBficture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixtute.destroy()
    request.addfinalizer(fin)
    return dbfixtute


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption('--check_ui')



def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')
    parser.addoption('--check_ui', action='store_true')


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            TestData = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, TestData, ids=[str(x) for x in TestData])
        elif fixture.startswith('json_'):
            TestData = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, TestData, ids=[str(x) for x in TestData])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).TestData


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json' % file)) as f:
        return jsonpickle.decode(f.read())