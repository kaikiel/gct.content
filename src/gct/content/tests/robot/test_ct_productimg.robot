# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s gct.content -t test_productimg.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src gct.content.testing.GCT_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/gct/content/tests/robot/test_productimg.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a ProductIMG
  Given a logged-in site administrator
    and an add ProductIMG form
   When I type 'My ProductIMG' into the title field
    and I submit the form
   Then a ProductIMG with the title 'My ProductIMG' has been created

Scenario: As a site administrator I can view a ProductIMG
  Given a logged-in site administrator
    and a ProductIMG 'My ProductIMG'
   When I go to the ProductIMG view
   Then I can see the ProductIMG title 'My ProductIMG'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ProductIMG form
  Go To  ${PLONE_URL}/++add++ProductIMG

a ProductIMG 'My ProductIMG'
  Create content  type=ProductIMG  id=my-productimg  title=My ProductIMG

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the ProductIMG view
  Go To  ${PLONE_URL}/my-productimg
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ProductIMG with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ProductIMG title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
