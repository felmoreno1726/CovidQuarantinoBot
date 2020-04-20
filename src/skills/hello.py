from interface import implements

from src.skills.interface import SkillInterface

class HelloSkill(implements(SkillInterface)):

    name = "HelloSkill"
    invocation_name = 'hello'

    def launch(self, state):
        starting_prompt = "Hi, my name is Covid Quarantino. I'm your friendly chatbot. What is your name?"
        self.state = state
        return starting_prompt

    def get_functionality(self):
        return "HelloSkill welcomes a new user to the sytem. "

    def query(self, prompt):
        #only expects to get a user response
        self.state['username'] = prompt
        return 'Nice to meet you {}'.format(prompt) 

    def exit_routine(self):
        #Hello skill ends with a general prompt to continue engaging the user in conversation.
        exit_message = "How are you?"
        return exit_routine
