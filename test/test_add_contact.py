# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(First_name="test",
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
                        Notes="-")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)