from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <First_name>, <Middle_name>, <Last_name>, <Nickname>, <Title>, <Company>, <Address>, <Home>, <Mobile>, <Work>, <Fax>, <E_mail>, <E_mail2>, <E_mail3>, <Homepage>, <Birthday_day>, <Birthday_month>, <Birthday_year>, <Anniversary_day>, <Anniversary_month>, <Anniversary_year>, <Address_Secondary>, <Home_Secondary> and <Notes>')
def new_contact(First_name, Middle_name, Last_name, Nickname, Title, Company, Address, Home, Mobile, Work, Fax, E_mail, E_mail2, E_mail3, Homepage, Birthday_day, Birthday_month, Birthday_year, Anniversary_day, Anniversary_month, Anniversary_year, Address_Secondary, Home_Secondary, Notes):
    return Contact(First_name=First_name, Middle_name=Middle_name, Last_name=Last_name, Nickname=Nickname, Title=Title, Company=Company, Address=Address, Home=Home, Mobile=Mobile, Work=Work, Fax=Fax, E_mail=E_mail, E_mail2=E_mail2, E_mail3=E_mail3, Homepage=Homepage, Birthday_day=Birthday_day, Birthday_month=Birthday_month, Birthday_year=Birthday_year, Anniversary_day=Anniversary_day, Anniversary_month=Anniversary_month, Anniversary_year=Anniversary_year, Address_Secondary=Address_Secondary, Home_Secondary=Home_Secondary, Notes=Notes)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(First_name='name1', Middle_name='Middle_name1', Last_name='Last_name1'))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@given('the index of a random contact')
def index_random_contact(non_empty_contact_list, random_contact):
    return non_empty_contact_list.index(random_contact)


@when('i add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@when('i delete the contact from the list')
def del_random_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)


@when('i edit the contact from the list')
def edit_random_contact(app, random_contact):
    edit_contact = Contact(First_name="EDIT", Last_name="EDIT2")
    edit_contact.id = random_contact.id
    app.contact.edit_by_id(edit_contact)


@then('the new contact list is equal to the old list with the contact')
def virify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then('the new contact list is equal to the old list without deleted contact')
def virify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@then('the new contact list is equal to the old list with the changed contact')
def virify_contact_edited(db, contact_list, random_contact, index_random_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    index = index_random_contact
    old_contacts[old_contacts.index(random_contact)] = new_contacts[index_random_contact]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)