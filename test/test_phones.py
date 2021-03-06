from model.contact import Contact
import re


def test_phones_on_home_page(app):
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
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
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
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.Home == contact_from_edit_page.Home
    assert contact_from_view_page.Mobile == contact_from_edit_page.Mobile
    assert contact_from_view_page.Work == contact_from_edit_page.Work
    assert contact_from_view_page.Home_Secondary == contact_from_edit_page.Home_Secondary


def clear(x):
    return re.sub("[()  -]", "", x)


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.Home, contact.Mobile, contact.Work, contact.Home_Secondary]))))


def merge_mail_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x is not None and x != '',
                            [contact.E_mail, contact.E_mail2, contact.E_mail3]))