class Player(object):
    #name, team, status, and points for the day
    name=""
    team=""
    status=True
    points=0
    def __init__(self,name, team, status, points):
        self.name=name
        self.team=team
        self.status=status
        self.points=points

