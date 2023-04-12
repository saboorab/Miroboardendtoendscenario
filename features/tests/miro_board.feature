Feature: Miro board verification
    As a QA,
    I want to automate miro board
    So that I can share with other users

  Scenario Outline: Validate the sticker creation with different users
    Given we have <userA> with <pass1>and <main_url>
    When user A login into Miro
    And  Create new "board"
    Then board should be created succesfully with <userA> login
    When user goto <boards_url>
    And user open the <board_name> created
    And user navigate to left toolbar and search for "Stickers and Emojis"
    And user clicks on "Stickers"
    And user drag any sticker from the "Stickers and Emojis" toolbar to the board
    And user share the board with the second user
    Then the share rights will be provided successfully with "201" response
    When <userA> gets logged out
    And  we have <userB> with <pass2>and <main_url>
    Then board shared by user 1 should open successfully for the user 2 as well with the same sticker and sticker should be visible to the user[UI]
    Examples:
      | main_url                | userA                  | userB            | pass1          | pass2         | board_name | boards_url                      |
      | https://miro.com/login/ | nehalamumtaz@gmail.com | 07se81@gmail.com | 2818compatible | 2818compatible| board      | https://miro.com/app/dashboard/ |