#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## greet + happy path 1
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## greet + happy path 2
* greet: hi there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## greet + sad path 1 + comedy
* greet: hi bot
  - utter_greet
* mood_unhappy: I'm doing awful
  - utter_cheer_up
* affirm: yes, please
  - action_comedy_time
  - utter_did_that_help

## greet + sad path 2 + comedy
* greet: Hi covid bot
  - utter_greet
* mood_unhappy: it is bad
  - utter_cheer_up
* affirm: oh yes I do
  - utter_did_that_help
  - utter_goodbye

## greet + sad path 3 + no comedy
* greet: hi quarantino bot
  - utter_greet
* mood_unhappy: very terrible
  - utter_cheer_up
* deny: no, I don't

## greet + sad path 4 + no comedy
* greet: hello bot
  - utter_greet
* mood_unhappy: I'm sad
  - utter_cheer_up
* deny: no, I don't

## positive remark 1
* positive_feedback: You are amazing, Covid
  - uttter_happy

## positive remark 2
* positive_feedback: You are a great bot
  - utter_happy

## negative remark 1
* negative_feedback: I don't like you
  - utter_apologies

* negative_feedback: You are awful
  - utter_apologies

## bot challenge 1
* bot_challenge: are you really a chatbot?
  - utter_iamabot

## bot challenge 2
* bot_challenge: are you really a human?
  - utter_iambot

## help message 1
* help: I want help
  - utter_help_message

## help message 2
* help: I need your help
  - utter_help_message

## chitchat 1
* out_of_scope: What did you eat for breakfast?
  - action_chitchat

## chitchat 2
* out_of_scope: What is the meaning of life?
  - action_chitchat

## covid screening 1
* covid_screen: Evaluate me for Covid-19
  - screening_form
  - form{"name": "screening_form"}
  - slot{"q1_answer": false}
  - slot{"q2_answer": false}
  - slot{"q3_answer": false}
  - slot{"q4_answer": false}
  - form{"name": null}

## covid screening 2
* covid_screen: Can you evaluate me for Covid?
  - screening_form
  - form{"name": "screening_form"}
  - slot{"q1_answer": false}
  - slot{"q2_answer": false}
  - slot{"q3_answer": false}
  - slot{"q4_answer": false}
  - form{"name": null}
