*** Setting ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  First_namebns  Middle_namewX  Last_namehyF  Nicknamecy  Title  CompanyfwN  Addressk  +76141945609  +77977554767  +77022297221  +73477236564  1@mail.ru  L@mail.ru  z@mail.ru  www.HomepageA.ru  24  February  1954  18  March  1914  Address_SecondaryFJ  +71274410888  NotesYF>
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Edit contact
    #Получаем изначальный список групп
    ${old_list}=  Get Contact List
    #Выбираем рандомно группу
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    #Создаем группу для изменения
    ${edit_contact}=  New Contact  EDIT  EDIT  Last_namehyF  Nicknamecy  Title  CompanyfwN  Addressk  +76141945609  +77977554767  +77022297221  +73477236564  1@mail.ru  L@mail.ru  z@mail.ru  www.HomepageA.ru  24  February  1954  18  March  1914  Address_SecondaryFJ  +71274410888  NotesYF>
    #Изменияем группу
    Edit Contact  ${contact}  ${edit_contact}
    #Получаем новый список групп
    ${new_list}=  Get Contact List
    #Удаляем старую группу
    Remove Values From List  ${old_list}  ${contact}
    #Добавляем измененную группу
    ${edit_group}=  Get From List  ${new_list}  ${index}
    Append To List  ${old_list}  ${edit_contact}
    #Сравниваем списки
    Group Lists Should Be Equal  ${new_list}  ${old_list}



