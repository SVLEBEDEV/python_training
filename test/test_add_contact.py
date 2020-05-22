# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix):
    symbols = str(string.digits)
    return prefix + ''.join([random.choice(symbols) for i in range(10)])


def random_mail(maxlen, postfix):
    symbols = string.ascii_letters + string.digits
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix

month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']
TestData = [Contact(First_name=random_string('First_name', 5),
                    Middle_name=random_string('Middle_name', 5),
                    Last_name=random_string('Last_name', 5),
                    Nickname=random_string('Nickname', 5),
                    Title=random_string('Title', 5),
                    Company=random_string('Company', 5),
                    Address=random_string('Address', 5),
                    Home=random_phone('+7'),
                    Mobile=random_phone('+7'),
                    Work=random_phone('+7'),
                    Fax=random_phone('+7'),
                    E_mail=random_mail(5, '@mail.ru'),
                    E_mail2=random_mail(5, '@mail.ru'),
                    E_mail3=random_mail(5, '@mail.ru'),
                    Homepage='www.'+ random_string('Homepage', 5) +'.ru',
                    Birthday_day=str(random.randint(1, 31)), Birthday_month=month[random.randint(0, 11)], Birthday_year=str(random.randint(1900, 2020)),
                    Anniversary_day=str(random.randint(1, 31)), Anniversary_month=month[random.randint(0, 11)], Anniversary_year=str(random.randint(1900, 2020)),
                    Address_Secondary=random_string('Address_Secondary', 5),
                    Home_Secondary=random_phone('+7'),
                    Notes=random_string('Notes', 5)) for i in range(2)]


@pytest.mark.parametrize('contact', TestData, ids=[repr(x) for x in TestData])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)