from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted

from utils.read_jokes import read_random_joke
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

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
        if username is not None:
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
