import re
from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0:
            return
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.form_filling(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def form_filling(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.First_name)
        self.change_field_value('middlename', contact.Middle_name)
        self.change_field_value('lastname', contact.Last_name)
        self.change_field_value('nickname', contact.Nickname)
        self.change_field_value('title', contact.Title)
        self.change_field_value('company', contact.Company)
        self.change_field_value('address', contact.Address)
        self.change_field_value('home', contact.Home)
        self.change_field_value('mobile', contact.Mobile)
        self.change_field_value('work', contact.Work)
        self.change_field_value('fax', contact.Fax)
        self.change_field_value('email', contact.E_mail)
        self.change_field_value('email2', contact.E_mail2)
        self.change_field_value('email3', contact.E_mail3)
        self.change_field_value('homepage', contact.Fax)
        self.change_field_value('fax', contact.Homepage)
        self.change_field_value_list('bday', contact.Birthday_day)
        self.change_field_value_list('bmonth', contact.Birthday_month)
        self.change_field_value('byear', contact.Birthday_year)
        self.change_field_value_list('aday', contact.Anniversary_day)
        self.change_field_value_list('amonth', contact.Anniversary_month)
        self.change_field_value('ayear', contact.Anniversary_year)
        self.change_field_value('address2', contact.Address_Secondary)
        self.change_field_value('phone2', contact.Home_Secondary)
        self.change_field_value('notes', contact.Notes)

    def change_field_value_list(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_new_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0:
            return
        wd.find_element_by_link_text("add new").click()

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_first(self):
        self.select_by_index(0)

    def edit_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_edit_by_index(index)
        self.form_filling(new_group_data)
        wd.find_element_by_name('update').click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first(self, new_group_data):
        self.edit_by_index(0, new_group_data)

    def open_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for el in wd.find_elements_by_xpath('//tr[@name="entry"]'):
                Last_name = el.find_elements_by_css_selector('td')[1].text
                First_name = el.find_elements_by_css_selector('td')[2].text
                all_phones = el.find_elements_by_css_selector('td')[5].text.splitlines()
                id = el.find_element_by_css_selector('input').get_attribute('id')
                self.contact_cache.append(Contact(First_name=First_name,
                                                  Last_name=Last_name,
                                                  id=id,
                                                  Home=all_phones[0],
                                                  Mobile=all_phones[1],
                                                  Work=all_phones[2],
                                                  Home_Secondary=all_phones[3]))
        return list(self.contact_cache)

    def open_details_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_by_index(index)
        wd.find_elements_by_xpath('//img[@title="Details"]')[index].click()

    def open_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_by_index(index)
        wd.find_elements_by_xpath('//img[@alt="Edit"]')[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_by_index(index)
        Last_name = wd.find_element_by_name('firstname').get_attribute('value')
        First_name = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        Home = wd.find_element_by_name('home').get_attribute('value')
        Mobile = wd.find_element_by_name('mobile').get_attribute('value')
        Work = wd.find_element_by_name('work').get_attribute('value')
        Home_Secondary = wd.find_element_by_name('phone2').get_attribute('value')
        return Contact(Last_name=Last_name,
                       First_name=First_name,
                       id=id,
                       Home=Home,
                       Mobile=Mobile,
                       Work=Work,
                       Home_Secondary=Home_Secondary)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_details_by_index(index)
        text = wd.find_element_by_id('content').text
        Home = re.search("H: (.*)", text).group(1)
        Mobile = re.search("M: (.*)", text).group(1)
        Work = re.search("W: (.*)", text).group(1)
        Home_Secondary = re.search("P: (.*)", text).group(1)
        return Contact(Home=Home,
                       Mobile=Mobile,
                       Work=Work,
                       Home_Secondary=Home_Secondary)

