Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
When I click on the "decoder-setting" and switch the value to "E"
and I click on the "shift-amount" and switch the value to "1"
and I click on the "letters" and enter "hi"
and I click "submit" button
Then I should see "ij" in the "decoded_message" 


Scenario: I can successfully decode a secret message
Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
When I click on the "decoder-setting" and switch the value to "D"
and I click on the "shift-amount" and switch the value to "1"
and I click on the "letters" and enter "ij"
and I click "submit" button
Then I should see "hi" in the "decoded_message"
    
