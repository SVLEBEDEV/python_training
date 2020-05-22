from sys import maxsize


class Contact:

    def __init__(self, First_name=None, Middle_name=None, Last_name=None, Nickname=None, Title=None, Company=None,
                 Address=None, Home=None, Mobile=None, Work=None, Fax=None, E_mail=None, E_mail2=None, E_mail3=None,
                 Homepage=None, Birthday_day=None, Birthday_month=None, Birthday_year=None, Anniversary_day=None,
                 Anniversary_month=None, Anniversary_year=None, Address_Secondary=None, Home_Secondary=None, Notes=None,
                 id=None, all_phones_from_home_page=None, all_mail_from_home_page=None):
        self.First_name = First_name
        self.Middle_name = Middle_name
        self.Last_name = Last_name
        self.Nickname = Nickname
        self.Title = Title
        self.Company = Company
        self.Address = Address
        self.Home = Home
        self.Mobile = Mobile
        self.Work = Work
        self.Fax = Fax
        self.E_mail = E_mail
        self.E_mail2 = E_mail2
        self.E_mail3 = E_mail3
        self.Homepage = Homepage
        self.Birthday_day = Birthday_day
        self.Birthday_month = Birthday_month
        self.Birthday_year = Birthday_year
        self.Anniversary_day = Anniversary_day
        self.Anniversary_month = Anniversary_month
        self.Anniversary_year = Anniversary_year
        self.Address_Secondary = Address_Secondary
        self.Home_Secondary = Home_Secondary
        self.Notes = Notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mail_from_home_page = all_mail_from_home_page

    def __repr__(self):
        return '%s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s' \
               ' ; %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s ; %s' \
               ' ; %s ; %s ; %s ; %s ; %s' % (self.First_name, self.Middle_name, self.Last_name, self.Nickname,
                                              self.Title, self.Company, self.Address, self.Home, self.Mobile, self.Work,
                                              self.Fax, self.E_mail, self.E_mail2, self.E_mail3, self.Homepage,
                                              self.Birthday_day, self.Birthday_month, self.Birthday_year,
                                              self.Anniversary_day, self.Anniversary_month, self.Anniversary_year,
                                              self.Address_Secondary, self.Home_Secondary, self.Notes, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.First_name == other.First_name \
               and self.Last_name == other.Last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize