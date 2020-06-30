Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <First_name>, <Middle_name>, <Last_name>, <Nickname>, <Title>, <Company>, <Address>, <Home>, <Mobile>, <Work>, <Fax>, <E_mail>, <E_mail2>, <E_mail3>, <Homepage>, <Birthday_day>, <Birthday_month>, <Birthday_year>, <Anniversary_day>, <Anniversary_month>, <Anniversary_year>, <Address_Secondary>, <Home_Secondary> and <Notes>
  When i add the contact to the list
  Then the new contact list is equal to the old list with the contact

  Examples:
  | First_name | Middle_name | Last_name | Nickname | Title | Company | Address | Home | Mobile | Work | Fax | E_mail | E_mail2 | E_mail3 | Homepage | Birthday_day | Birthday_month | Birthday_year | Anniversary_day | Anniversary_month | Anniversary_year | Address_Secondary | Home_Secondary | Notes>
  | First_namebns | Middle_namewX | Last_namehyF | Nicknamecy | Title | CompanyfwN | Addressk | +76141945609 | +77977554767 | +77022297221 | +73477236564 | 1@mail.ru | L@mail.ru | z@mail.ru | www.HomepageA.ru | 24 | February | 1954 | 18 | March | 1914 | Address_SecondaryFJ | +71274410888 | NotesYF>


Scenario Outline: Del random contact
  Given a non-empty contact list
  Given a random contact from the list
  When i delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact


Scenario Outline: Edit random contact
  Given a contact list
  Given a random contact from the list
  Given the index of a random contact
  When i edit the contact from the list
  Then the new contact list is equal to the old list with the changed contact