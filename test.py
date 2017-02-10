# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:23:25 2017

@author: 3202238
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:54:40 2017

@author: 3202238
"""



from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math

#Toolbox
class Position(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
    
    def my_position(self):
        return self.state.player_state(self.id_team, self.id_player).position
    
    def ball_position(self):
        return self.state.ball.position
    def ball_positionX(self):
        return self.state.ball.position.x
    def ball_positionY(self):
        return self.state.ball.position.y

    def position_but_adv(self):
        if self.id_team == 1:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(0,settings.GAME_HEIGHT/2.)
            
    def ball_vitesse(self):
        return self.state.ball.vitesse
    
    def ball_trajectoire(self):
        return self.state.ball_position() + self.state.ball_vitesse()*11
    def zone_tir(self):
        return (self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS
    
    def pos_j1(self):
         return self.state.player_state(self.id_team,1).position
         
    def pos_j2(self):
         return self.state.player_state(self.id_team,2).position        
#####################################################################################################
        
class Action(object) :
    def __init__(self, state):
        self.state = state
#        self.id_team = id_team
#        self.id_player = id_player
#        self.mon_but = Vector2D(0, settings.GAME_HEIGHT/2)
#        self.but_adv = Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
#        self.Position = Position
    def aller(self, p):
        return SoccerAction((p-self.state.my_position()), Vector2D())
    
    def aller_balle(self):
        return self.aller(self.state.ball_trajectoire())
        
    def shoot_but(self, p):
        if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.1)
    
    def degagement(self):
        if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):
            return SoccerAction(Vector2D(),Vector2D(self.state.position_but_adv())
        else:
            return self.aller(self.state.ball_position())
        
    def mini_shoot(self, p):
        if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.015)
        else :
            return self.aller(self.state.ball_position())
            
    def passe(self):
        if (self.state.id_player == 1):
                return self.shoot(self.state.pos_j2())
        else :
            return self.shoot(self.state.pos_j1())
    

        
    
        
            
    def dribbler(self):
        if (self.state.id_team == 1):
            if zone_tir() and self.state.ball_positionX() >110:
                return self.shoot(self.state.position_but_adv())            
            elif ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):       
                return self.aller(self.state.ball_position())+ self.mini_shoot(self.state.position_but_adv())
            else:
                return self.aller(self.state.ball_position())
        else: 
            if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS) and self.state.ball_positionX() <50:
                return self.shoot(self.state.position_but_adv())
            elif ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):       
                return self.aller(self.state.ball_position())+ self.mini_shoot(self.state.position_but_adv())
            else:
                return self.aller(self.state.ball_position())
    def defense(self):
        if (self.state.id_team ==1):
            if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS) and self.state.ball_positionX()  < 70 : 
                return self.aller(self.state.ball_position()+self.state.vitesse_balle()*11) +self.shoot(self.state.position_but_adv())
            elif self.state.ball_positionX() < 70 :
                return self.aller(self.state.ball_position()+self.state.vitesse_balle()*11)    
        
        else:
            if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS) and self.state.ball_positionX()  > 110 : 
                return self.aller(self.state.ball_position()+self.state.vitesse_balle()*11) + self.shoot(self.state.position_but_adv())
            elif self.state.ball_positionX() > 110 :
                return self.aller(self.state.ball_position()+self.state.vitesse_balle()*11)   
                
                
    def gardien(self):
        if (self.state.id_team ==1):
            if (self.state.ball_positionX()>40) :
                return  self.aller(Vector2D(10,self.state.ball_positionY()))
            else :
                if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS) :
                    return self.aller(self.state.ball_position()+self.state.vitesse_balle()*11) +self.shoot(self.state.position_but_adv()) 

