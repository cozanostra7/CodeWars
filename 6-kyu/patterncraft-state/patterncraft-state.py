class SiegeState:
    def __init__(self):
        self.canMove = False
        self.damage = 20
​
class TankState:
    def __init__(self):
        self.canMove = True
        self.damage = 5
​
class Tank:
    def __init__(self):
        self.state = TankState()
​
  
    @property
    def canMove(self):
        return self.state.canMove
​
    def can_move(self):
        return self.state.canMove
  
    def damage(self):
        return self.state.damage