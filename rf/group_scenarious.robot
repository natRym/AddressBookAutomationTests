*** Settings ***
Library  rf.AddressBook
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new group
   ${old_list}=  Get Group List
   Create Group  name1  header1  footer1
   ${new_list}=  Get Group List