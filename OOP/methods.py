class FootBallTeam:
    count = 0
    def __init__(self, name):
        self.name = name
        FootBallTeam.count += 1
    
    @classmethod
    def get_count(cls):
        return f"Total football teams: {cls.count}"
    
    @staticmethod
    def info():
        return "This is a football team class"
    
team_one = FootBallTeam("Real Madrid")
team_two = FootBallTeam("Barcelona")
team_three = FootBallTeam("Bayern Munich")
print(FootBallTeam.get_count())