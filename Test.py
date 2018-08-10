import  unittest 
from Team import Team
from Players import Player
class TestTeams(unittest.TestCase):
    def setUp(self):
        self.players=[]
        player1=Player("Messi", "Barcelona", True, 100)
        player2=Player("Ronaldo", "Madrid", True, 80)
        player3=Player("Maradona", "Barcelona", True, 100)
        player4=Player("Tevez", "Boca", False, 50)
        self.players.append(player1)
        self.players.append(player2)
        self.players.append(player3)
        self.players.append(player4)
        self.teams=Team.create_teams(self.players)
    
    def test_compare_teams(self):
        player1=Player("Messi", "Barcelona", True, 100)
        player2=Player("Ronaldo", "Madrid", True, 80)
        player3=Player("Maradona", "Barcelona", True, 100)
        player4=Player("Tevez", "Boca", False, 50)

        newPlayers=[]
        #I add the players in diferent orders
        newPlayers.append(player2)        
        newPlayers.append(player1)
        newPlayers.append(player4)        
        newPlayers.append(player3)
        self.assertEqual(str(self.teams),str(Team.create_teams(newPlayers)))

    def test_add_one_player(self):
        player=Player("Marcos","No One",True,100)
        for team in self.teams:
            self.assertEqual(False,team.add_payer(player))
    

        
        
        