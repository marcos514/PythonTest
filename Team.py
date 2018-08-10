from Players import Player


class Team(object):
    player_list=[]
    points=0
    team_name=""
    def __init__(self,name):
        self.team_name=name

    def __str__(self):
        return self.team_name +" - "+ str(self.points)

    def __repr__(self):
        return str(self)
    
    def add_payer(self,player):
        if(player.team==self.team_name):
            self.player_list.append(player)
            if(player.status==True):
                self.points+=player.points
            return True
        else:
            return False


    @staticmethod
    def add_player_to_his_team(teamList,player):
        try:
            for p in teamList:
                if(p.add_payer(player)):
                    return True
    
            newTeam=Team(player.team)
            newTeam.add_payer(player)
            teamList.append(newTeam)
            
            return True
        except :
            return False



    @staticmethod
    def create_teams(players):
        try:
            teamList=[]
            errors=0
            for p in players:
                validator=True
                validator=Team.add_player_to_his_team(teamList,p)
                if(validator==False):
                    errors+=1
                    
            return Team.sort_teams(teamList)
        except :
            return False




    @staticmethod
    def sort_teams(teamList):
        teamList.sort(Team.compare_points)
        return teamList
    

    @staticmethod
    def compare_points(x,y):
        if(x.points>y.points):
            return -1
        elif x.points<y.points:
            return 1
        else:
            return 0




#player=Player("Marcos", "aa", True, 100)
#aaa=[]
#aaa.append(player)
#player=Player("Marcos", "Ind", True, 80)
#aaa.append(player)


#player=Player("Marcos", "Boca", True, 100)
#aaa.append(player)


#player=Player("Marcos", "aa", False, 50)
#aaa.append(player)

#ret=Team.create_teams(aaa)
#print ret

#print Team.sort_teams(ret)
#futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"), (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]
#futbolistasTup.sort(key=lambda player: poins[0])
#print "Imprimimos las lista ordenada por dorsal:"
#print futbolistasTup
    