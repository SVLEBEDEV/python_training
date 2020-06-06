from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


orm = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_random_contact_to_random_group(app, db):
    contact = None
    add_to_group = None
    all_groups = db.get_group_list()
    if len(all_groups) == 0:
        app.group.create(Group(name="1", header="TEST_1.1", footer="TEST_1.2"))
        all_groups = db.get_group_list()
    for group in all_groups:
        contacts = orm.get_contacts_not_in_group(group)
        if len(contacts) > 0:
            contact = contacts[0]
            add_to_group = group
            break
    if contact is None:
        app.contact.create(Contact(First_name="test",
                                   Middle_name="test1",
                                   Last_name="test2",
                                   Nickname="test3",
                                   Title="test4",
                                   Company="test5",
                                   Address="SPB",
                                   Home="12345",
                                   Mobile="12345",
                                   Work="12345",
                                   Fax="-",
                                   E_mail="111@mail.ru",
                                   E_mail2="-",
                                   E_mail3="-",
                                   Homepage="www.test.ru",
                                   Birthday_day="2", Birthday_month="January", Birthday_year="1993",
                                   Anniversary_day="15", Anniversary_month="December", Anniversary_year="2001",
                                   Address_Secondary="-",
                                   Home_Secondary="12345",
                                   Notes="-"))
        contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
        contact = contacts[len(contacts)-1]
    old_list_contacts = orm.get_contacts_in_group(add_to_group)
    app.contact.add_random_contact_to_random_group(contact, add_to_group)
    new_list_contacts = orm.get_contacts_in_group(add_to_group)
    assert len(old_list_contacts) + 1 == len(new_list_contacts) and new_list_contacts.count(contact) == 1


