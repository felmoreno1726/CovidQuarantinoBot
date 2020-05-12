import logging
import torch
from transformers import AutoModelWithLMHead, AutoTokenizer
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted

from utils.read_jokes import read_random_joke

logger = logging.Logger(__name__)

class ActionGreetUser(Action):
    """
    Revertible mapped action for utter_greet
    This reverts the flow of the conversation if a uses interjects the conversation with a greet.
    """

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot('username')
        print('username: ', username)
        logger.debug('username: ' + str(username))
        if username is None:
            dispatcher.utter_template("utter_introduce", tracker)
        else:
            dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]

class ActionStoryTime(Action):
    """
    This action reads a story from a list of stories, and gives one to the user.
    """

    def name(self):
        return "action_story_tell"

    def run(self, dispatcher, tracker, domain):
        story = "Hey this is a story"
        dispatcher.utter_message(text=story)
        return []

class ActionComedyTime(Action):
    """
    This action tell a one-liner joke from a list of jokes
    """

    def name(self):
        return "action_comedy_time"

    def run(self, dispatcher, tracker, domain):
        #joke = "This is a joke. haha..."
        joke = read_random_joke()
        dispatcher.utter_message(text=joke)
        return []


# Chitchat model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-large")
#initialize chitchat history
chat_history_ids = None 

class ActionDefault(Action):
    """
    This action feeds the user request to 
    """
    
    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):
        global tokenizer, model, chat_history_ids
        user_utterance = tracker.latest_message["text"]
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(user_utterance + tokenizer.eos_token, return_tensors='pt')
        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids
        # generated a response while limiting the total chat history to 1000 tokens
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        logger.debug(str(chat_history_ids))
        print(str(chat_history_ids))
        response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        dispatcher.utter_message(text=response)
        return [UserUtteranceReverted()]

class CovidScreeningForm(FormAction):
    """
    This form asks for the required questions of the covid screening a returns appropriate follow-up advice.
    """

    def name(self):
        return "screening_form"

    @staticmethod
    def required_slots(tracker):
        """
        Requires a list of the slots to be filled for the form
        """
        return ["q1_answer", "q2_answer", "q3_answer", "q4_answer"]

    def slot_mappings(self):
        """
        Maps intents to slot values for the form
        """
        mappings = {
                'q1_answer' : [self.from_intent(intent='affirm', value=True), self.from_intent(intent='deny', value=False)],
                'q2_answer' : [self.from_intent(intent='affirm', value=True), self.from_intent(intent='deny', value=False)],
                'q3_answer' : [self.from_intent(intent='affirm', value=True), self.from_intent(intent='deny', value=False)],
                'q4_answer' : [self.from_intent(intent='affirm', value=True), self.from_intent(intent='deny', value=False)]
        }
        return mappings

    def submit(self, dispatcher, tracker, domain):
        q1_answer = tracker.get_slot('q1_answer')
        q2_answer = tracker.get_slot('q2_answer')
        q3_answer = tracker.get_slot('q3_answer')
        q4_answer = tracker.get_slot('q4_answer')
        if q1_answer or q2_answer:
            #High risk message
            dispatcher.utter_template("utter_medical_and_state_dept", tracker)
        elif q3_answer or q4_answer:
            #Low risk message
            dispatcher.utter_template("utter_medical", tracker)
        else:
            #No asses risk. Give advice if anything arises
            dispatcher.utter_template("utter_no_risk", tracker)
        dispatcher.utter_template('utter_medical_visit_instructions', tracker)
        return []
