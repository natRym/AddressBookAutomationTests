*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***

Add new contact
   ${old_list}=  Get Contact List
   ${contact}=  New Contact  firstname1  lastname1  company1
   Create Contact  ${contact}
   ${new_list}=  Get Contact List
   append to list  ${old_list}  ${contact}
   Contact Lists Should be Equal  ${new_list}  ${old_list}


Delete Contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    remove values from list  ${old_list}  ${contact}
    Contact Lists Should be Equal  ${new_list}  ${old_list}


Edit Contact
   ${old_list}=  Get Contact List
   ${contact}=  Edit Contact Data  firstname2  lastname2  company2
   Edit Contact  ${contact}
   ${new_list}=  Get Contact List
   append to list  ${old_list}  ${contact}
   Contact Lists Should be Equal  ${new_list}  ${old_list}
