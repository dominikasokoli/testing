*** Settings ***
Library   SeleniumLibrary

*** Variables ***
${BROWSER}   Firefox
${VALID USER}   
${VALID PASSWORD}   
${URLMAILBOX}   https://profil.wp.pl/login.html?zaloguj=poczta
${FIELD LOGIN}   //*[@id="login"]
${FIELD PASSWORD}   //*[@id="password"]
${BUTTON}   css:.nSubmit

*** Test Cases ***
Mailbox login test
  Open Firefox browser
  Open website www.wp.pl
  Log in to Emailbox
  Check if word received is there
  Close browser

*** Keywords ***
Open Firefox browser
  Open browser   about:blank   ${BROWSER}
Open website www.wp.pl
  Go to    ${URLMAILBOX}
Log in to Emailbox
  Input text   ${FIELD LOGIN}   ${VALID USER}
  Input text   ${FIELD PASSWORD}   ${VALID PASSWORD}
  Click element   ${button}
Check if word received is there
  Page Should Contain   Odebrane
Close browser
  Close All Browsers
