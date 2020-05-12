## Introduction + happy mood
* introduce
  - utter_greet
* mood_great
  - utter_happy

## Introduction + sad mood + good cheer
* introduce
  - utter_greet
* mood_unhappy
  - utter_cheer_up
* affirm
  - action_comedy_time
  - utter_did_that_help

## Introduction + sad mood + good cheer
* introduce
  - utter_introduce
* mood_unhappy
  - utter_cheer_up
* deny

## positive remarks
* positive_feedback
  - utter_happy

* negative_feedback
  - utter_apologies

## Default 'chitchat' handler
* out_of_scope
  - action_chitchat

## bot challenge
* bot_challenge
  - utter_iamabot

## help message
* help
  - utter_help_message

## covid screening
* covid_screen
  - screening_form
  - form{"name": "screening_form"}
  - slot{"q1_answer": false}
  - slot{"q2_answer": false}
  - slot{"q3_answer": false}
  - slot{"q4_answer": false}
  - form{"name": null}

