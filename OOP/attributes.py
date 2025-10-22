class EnglishFootBallClub:
    league = "EPL" # class  attributes
    def __init__(self, name, titles):
        self.name = name # instance attributes
        self.titles = titles
    
    def country(self):
        return f"{self.name} is in England"
        

team_one = EnglishFootBallClub("Chelsea", 14)
print(team_one.name)
print(team_one.league)
print(team_one.country())