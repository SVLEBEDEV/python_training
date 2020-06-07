import random
from model.contact import Contact
from model.group import Group


def test_del_random_contact_to_random_group(app, orm):
    contact = None
    add_to_group = None
    all_groups = orm.get_group_list()
    if len(all_groups) == 0:
        app.group.create(Group(name="1", header="TEST_1.1", footer="TEST_1.2"))
        app.contact.add_random_contact_to_random_group(random.choice(orm.get_contact_list()), random.choice(orm.get_group_list()))
        all_groups = orm.get_group_list()
    for group in all_groups:
        contacts = orm.get_contacts_in_group(group)
        if len(contacts) > 0:
            contact = contacts[0]
            add_to_group = group
            break
    if contact is None and orm.get_contact_list() == 0:
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
        contact = orm.get_contact_list()[0]
        add_to_group = random.choice(orm.get_group_list())
        app.contact.add_random_contact_to_random_group(contact, add_to_group)
    elif contact is None and orm.get_contact_list() != 0:
        contact = random.choice(orm.get_contact_list())
        add_to_group = random.choice(orm.get_group_list())
        app.contact.add_random_contact_to_random_group(contact, add_to_group)
    old_list_contacts = orm.get_contacts_in_group(add_to_group)
    app.contact.del_random_contact_to_random_group(contact, add_to_group)
    new_list_contacts = orm.get_contacts_in_group(add_to_group)
    assert len(old_list_contacts) - 1 == len(new_list_contacts) and new_list_contacts.count(contact) == 0