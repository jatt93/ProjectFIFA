from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D,SoccerState, SoccerAction
from soccersimulator import settings
import math
import toolbox_Action


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))
        

def fonceur(m_action):
     return m_action.aller(m_pos.ball_position()) + m_action.shoot(m_pos.position_but_adv())
     
     ## Strategie d'attaque
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
    def compute_strategy(self,state,id_team,id_player):        
        m_pos = toolbox_Action.Position(state, id_team, id_player)
        m_action= toolbox_Action.Action(m_pos)
        return m_action.aller(m_pos.ball_position()) + m_action.shoot(m_pos.position_but_adv())
        #return fonceur(Action(state, id_team, id_player))
#Stategie de defense
#class DefenseStrategy(Strategy):
#    def __init__(self):
#        Strategy.__init__(self,"Defense")
#    def compute_strategy(self, state, id_team, id_player):
#            return defense(Action(state, id_team, id_player))
       


#def dribble(m_action):
#    return m_action.dribbler()
#    
#def attaque(m_action):
#    return m_action.attaque()
#    
#def defense(m_action):
#     if Position.state.ball.position.x > 110:
#            return SoccerAction(Position.ball_position() - Position.my_position(),Vector2D(-50, 0))
#Stategie de defense
class DefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = toolbox_Action.Position(state, id_team, id_player)
        m_action= toolbox_Action.Action(m_pos)
        return m_action.defense()

## Strategie d'attaque
#class DribbleStrategy(Strategy):
#    def __init__(self):
#        Strategy.__init__(self,"Dribble")
#    def compute_strategy(self,state,id_team,id_player):        
#        m_action = Action(state, id_team, id_player)
#        return dribble(m_action)
        


##class AttaqueStrategy(Strategy):
# {   def __init__(self):
#        Strategy.__init__(self,"Attaque")
#    def compute_strategy(self,state,       
#        m_action = Action(state, id_team, id_player)
#        if state.ball.position.x > 110: 
#            return dribble(m_action)
#            
#        else :
#            return attaque(m_action)


#Strategie dribble
class AttaqueStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ronaldinho")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = toolbox_Action.Position(state, id_team, id_player)
        m_action= toolbox_Action.Action(m_pos)
        return m_action.dribbler()

### Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")

#team1.add("Alexis",AttaqueStrategy())
team1.add("Mertesacker",DefenseStrategy()) #Strategie qui ne fait rien

team2.add("Pique",DefenseStrategy())   #Strategie aleatoire
team2.add("Neymar",AttaqueStrategy())
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
##Jouer sans afficher
simu.start()