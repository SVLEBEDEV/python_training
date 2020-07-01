import json
import os.path
from fixture.application import Application
from fixture.db import DBficture
from model.group import Group


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUIT'

    def __init__(self, config="target.json", browser="firefox"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, baseURL=web_config['baseURL'])
        db_config = self.target['db']
        self.dbfixture = DBficture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_by_id(group.id)
    
    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)