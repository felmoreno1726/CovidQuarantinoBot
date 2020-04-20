
class Skills():

    def __init__(self):
        _skills = self.initialize_skills()
        self._skills = _skills
        self.invocation_names = {_skill.invocation_name: _skill for _skill in _skills}
        self.names = {_skill.name: _skill for _skill in _skills}

    @staticmethod    
    def initialize_skills():
        skills_list = []
        #makes skills available to the chatbot framework
        from src.skills.hello import HelloSkill
        skills_list.append(HelloSkill())
        #from src.skills.covid_diagnosis import CovidDiagnosisSkill; skill.append[CovidDiagnoisSkill]
        #from src.skills.flight_scheduler import FlightSchedulerSkill; skill.append[FlightSchedulerSkill]
        return skills_list

skills = Skills()
