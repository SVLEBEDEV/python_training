from datetime import datetime
from pony.orm import *
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()

    def convet_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convet_groups_to_model(list(select(g for g in ORMFixture.ORMGroup)))

    def convet_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), First_name=contact.firstname, Last_name=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convet_contacts_to_model(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None)))