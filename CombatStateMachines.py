class PlayerStateBase:
    def __init__(self, context):
        self.context = context

    def OnEnter(self):
        pass

class Tired_State(PlayerStateBase):
    def OnEnter(self):
        if self.player_ref._stamina > 10:
            print("act")
            return "active"
        else:
            return "tired"
class Active_State(PlayerStateBase):
    def OnEnter(self):
        if self.player_ref._stamina <= 10:
            print("tir")
            return "tired"
        else:
            return "active"
class Strength_State(PlayerStateBase):
    def OnEnter(self):
        if self.player_ref._strength != True:
            print("str")
            return "tired"
        else:
            return "strength"
class PlayerBuffStateMachine:
    def __init__(self, player_ref):
        self.states = {
            "tired" : Tired_State(self),
            "active" : Active_State(self),
            "strength": Strength_State(self),
            }
        self.currentState = "active"
        self.player_ref = player_ref

    def TransitionState(self):
        nextstate = self.states[self.currentState].OnEnter()
        if nextstate != self.currentState:
            nextstate = self.currentState
        return True
    





                                            # TURN TRACKER STATE






class CombatTurnBase:
    def __init__(self, context):
        self.context = context

    def OnEnter(self):
        pass

class EnemyTurn(CombatTurnBase):
    def OnEnter(self):
        if self.player_red._player_combat_turn ==  True:
            return "player"
        else:
            return "enemy"
class PlayerTurn(CombatTurnBase):
    def OnEnter(self):
        if self.player_ref._player_combatr_turn == False:
            return "enemy"
        else:
            return "player"
class CombatTurnAlternatingStateMachine:
    def __init__(self, player_ref):
        self.states = {
            "enemy" : EnemyTurn(self),
            "player" : PlayerTurn(self),
            }
        self.currentState = "player"
        self.player_ref = player_ref

    def TransitionState(self):
        nextstate = self.states[self.currentState].OnEnter()
        if nextstate != self.currentState:
            nextstate = self.currentState
        return True