# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
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
    app.contact.edit_first(Contact(First_name="EDIT", Birthday_day="15"))