# -*- coding: utf-8 -*-
from time import sleep
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(First_name="test",
                               Middle_name="test1",
                               Last_name="test2",
                               Nickname="test3",
                               Title="test4",
                               Company="test5",
                               Address="SPB",
                               Home="111-11-11",
                               Mobile="+7(111)111-11-11",
                               Work="222-22-22",
                               Fax="-",
                               E_mail="111@mail.ru",
                               E_mail2="-",
                               E_mail3="-",
                               Homepage="www.test.ru",
                               Birthday_day="2", Birthday_month="January", Birthday_year="1993",
                               Anniversary_day="15", Anniversary_month="December", Anniversary_year="2001",
                               Address_Secondary="-",
                               Home_Secondary="-",
                               Notes="-"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    sleep(3)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts