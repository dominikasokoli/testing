*** Settings ***
Library   library_python.py
Library   SSHLibrary
*** Variables ***
${NAME}   X
${NUMBER}   100
${REMOTE_HOST}   
${REMOTE_USERNAME}   
${REMOTE_PASSWORD}   

*** Test Cases ***
Automated Test
  Log To Console   Hello
Time
  Get Time   return year
Converting
  Convert To Integer   ${NUMBER}
Checking Name
  Log To Console   ${NAME}
Comunicating
  Print on screen  Test
Python library Check
  ${ADDING RESULT} =   adding two strings   AAA   BBB
  Should be equal   ${ADDING RESULT}   AAABBBBBBAAA
Checking command line test
  Establish Connection
  Enter credentials
  Execute Test Command
  Close Test Connection
  
*** Keywords ***
Print on screen
  [Arguments]   ${coms}
  log to console    ${coms}
Establish Connection
  Open Connection   ${REMOTE_HOST}
Enter credentials
  Login   ${REMOTE_USERNAME}   ${REMOTE_PASSWORD}
Execute Test Command
  ${OUTPUT} =   Execute Command   uname -a
  Should Contain   ${OUTPUT}   GNU/Linux
Close Test Connection
  Close All Connections
