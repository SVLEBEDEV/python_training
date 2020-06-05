from model.contact import Contact
import re


def test_check_contact(app, db):
    if app.contact.count() == 0:
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
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i] == contact_from_db[i]


def clear(s):
    return re.sub("[()  -]", "", s)


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.Home, contact.Mobile, contact.Work, contact.Home_Secondary]))))


def merge_mail_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x is not None and x != '',
                            [contact.E_mail, contact.E_mail2, contact.E_mail3]))