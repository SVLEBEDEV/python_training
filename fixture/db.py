import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DBficture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list_groups=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list_groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_groups

    def get_contact_list(self):
        list_contacts=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, '
                           'work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, '
                           'address2, phone2, notes from addressbook')
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax,
                 email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes) = row
                list_contacts.append(Contact(id=str(id),
                                             First_name=firstname,
                                             Middle_name=middlename,
                                             Last_name=lastname,
                                             Nickname=nickname,
                                             Title=title,
                                             Company=company,
                                             Address=address,
                                             Home=home,
                                             Mobile=mobile,
                                             Work=work,
                                             Fax=fax,
                                             E_mail=email,
                                             E_mail2=email2,
                                             E_mail3=email3,
                                             Homepage=homepage,
                                             Birthday_day=bday, Birthday_month=bmonth, Birthday_year=byear,
                                             Anniversary_day=aday, Anniversary_month=amonth, Anniversary_year=ayear,
                                             Address_Secondary=address2,
                                             Home_Secondary=phone2,
                                             Notes=notes))
        finally:
            cursor.close()
        return list_contacts

    def destroy(self):
        self.connection.close()