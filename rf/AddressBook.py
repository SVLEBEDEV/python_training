import json
import os.path
from fixture.application import Application
from fixture.db import DBficture
from model.group import Group
from model.contact import Contact


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

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

    def new_contact(self, First_name, Middle_name, Last_name, Nickname, Title, Company, Address, Home, Mobile, Work, Fax,
                    E_mail, E_mail2, E_mail3, Homepage, Birthday_day, Birthday_month, Birthday_year, Anniversary_day,
                    Anniversary_month, Anniversary_year, Address_Secondary, Home_Secondary, Notes):
        return Contact(First_name=First_name, Middle_name=Middle_name, Last_name=Last_name, Nickname=Nickname,
                       Title=Title, Company=Company, Address=Address, Home=Home, Mobile=Mobile, Work=Work, Fax=Fax,
                       E_mail=E_mail, E_mail2=E_mail2, E_mail3=E_mail3, Homepage=Homepage, Birthday_day=Birthday_day,
                       Birthday_month=Birthday_month, Birthday_year=Birthday_year, Anniversary_day=Anniversary_day,
                       Anniversary_month=Anniversary_month, Anniversary_year=Anniversary_year,
                       Address_Secondary=Address_Secondary, Home_Secondary=Home_Secondary, Notes=Notes)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def delete_group(self, group):
        self.fixture.group.delete_by_id(group.id)

    def delete_contact(self, contact):
        self.fixture.contact.delete_by_id(contact.id)

    def edit_group(self, group, new_group_data):
        new_group_data.id = group.id
        self.fixture.group.edit_by_id(new_group_data)

    def edit_contact(self, contact, new_contact_data):
        new_contact_data.id = contact.id
        self.fixture.contact.edit_by_id(new_contact_data)
    
    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)