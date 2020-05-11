## Greet already introduced
* greet
  - slot{"username":"name"}
  - utter_greet

## Introduction + greet + happy mood
* greet
  - utter_introduce
* introduce
  - utter_greet
* mood_great
  - utter_happy

## Introduction + greet + sad mood + good cheer
* greet
  - utter_introduce
* introduce
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## Introduction + greet + sad mood + good cheer
* greet
  - utter_introduce
* introduce
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## positive remarks
* positive
  - utter_positive

* negative
  - utter_negative

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
