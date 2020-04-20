import interface
from interface import Interface

class SkillInterface(Interface):
    
    #name = "SkillInterface"
    #invocation_name = "THIS SHOULD NEVER BE INVOKED."

    def launch(self, state):
        """
        Returns the launch prompt to the skill
        """
        pass

    def get_functionality(self):
        raise Exception("Interface method not implemented")

    def query(self, prompt):
        raise Exception("Interface method not implemented")

    def exit_routine(self):
        raise Exception("Interface method not implemented")

