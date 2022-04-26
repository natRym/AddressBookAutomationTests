Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <middlename>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact


  Examples:
  | firstname  | lastname  | middlename  |
  | firstname1 | lastname1 | middlename1 |
  | firstname2 | lastname2 | middlename2 |


Scenario: Delete a contact
  Given non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact
