import json, os
from warnings import warn
from interface import implements

from src.skills import skills
from src.skills.interface import SkillInterface


#class Chatbot(implements(SkillInterface)): ### Do we want to make the engine a skill?
class Chatbot():

    HELP_MESSAGE = "or just type anthing and press enter to chat with me."

    def __init__(self, reset, state_path="./state.json"):
        """
        reset (Bool): if set to true, resets the bot to its original state
        """
        self.state_path = state_path
        if reset or not os.path.exists(state_path):
            #initialize chatbot interecation
            self.state = {
                    'username': None,
                    'feeling' : None #Maybe initalize to neutral?
            }
            #Always start with Hello skill to welcome a new user
            self.active_skill = skills.names['HelloSkill']
        else:
            #reloads state from left off json
            with open(state_path) as state:
                state = json.load(state)
            self.active_skill = None

    def launch(self):
        if self.active_skill is not None:
            print('self.active_skill: ', self.active_skill)
            return self.active_skill.launch(self.state)
        else:
            #TODO what should be the default behaviour? Generate a conversation?
            warn("Default behaviour not implemented")
            return "Ask me anything"

    def get_functionality(self):
        """
        Lists the basic commands and functionality available to the chatbot.
        Lists available skills, invocation names and functionality of each.
        """
        message = "You can say: "
        for skill_activation in skills.activations.keys():
            message += skill_actication + ', '
            #"\'Help me book a flight\', \`Covid testing\` to trigger some of my useful skills, "
        message += HELP_MESSAGE
        return message

    def query(self, prompt):
        """
        prompt (String): user input to the chatbot
        Returns (String) text response back to the user's prompt.
        """
        #TODO we should also parse out special characters, and some words/tokens.
        #TODO call sentiment analysis API and update 'feeling' state
        prompt = prompt.lower()
        if self.active_skill is not None:
            response = self.active_skill.query(prompt)
        elif prompt == 'help':
            response = get_functionality()
        elif (skill := skills.invocation_names.get(prompt)) is not None:
            self.active_skill = skill(self.state)
            response = self.active_skill.launch()
        else:
            warn('General chatbot not yet implemented!')
            response = "I'm not smart enough to understand. Please donate coffee to the developers. Thanks! OwO"
        return response

    def exit_routine(self):
        """
        If a skill is active, exits the skill to return to main. Else, exits the main handler and stores the current state into state_path json file.
        """
        #save state
        with open(state_path, 'w') as state_file:
            json.dump(self.state, state_file)
        return