from random import choice
class BoggleDice:
  def __init__(self):
    self.dice = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
    self.dice[0][0]=['R','I','F','O','B','X']
    self.dice[0][1]=['I','F','E','H','E','Y']
    self.dice[0][2]=['D','E','N','O','W','S']
    self.dice[0][3]=['U','T','O','K','N','D']
    self.dice[1][0]=['H','M','S','R','A','O']
    self.dice[1][1]=['L','U','P','E','T','S']
    self.dice[1][2]=['A','C','I','T','O','A']
    self.dice[1][3]=['Y','L','G','K','U','E']
    self.dice[2][0]=['QU','B','M','J','O','A']
    self.dice[2][1]=['E','H','I','S','P','N']
    self.dice[2][2]=['V','E','T','I','G','N']
    self.dice[2][3]=['B','A','L','I','Y','T']
    self.dice[3][0]=['E','Z','A','V','N','D']
    self.dice[3][1]=['R','A','L','E','S','C']
    self.dice[3][2]=['U','W','I','L','R','G']
    self.dice[3][3]=['P','A','C','E','M','D']

  def getLetter(self,i,j):
    return choice(self.dice[i][j])