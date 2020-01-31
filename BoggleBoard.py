from tkinter import Tk,Label,font,Button,RAISED,SUNKEN
from functools import partial

from BoggleDice import BoggleDice

class BoggleBoard:
  def __init__(self,screen):
      #Variables used to keep track
      self.last_i = [None]
      self.last_j = [None]
      self.word = ''
      #Constants used in the interface
      TITLE="Boggle"
      BTN_WIDTH=5
      BTN_HEIGHT=2
      LETTER_FONT=font.Font(family='arial',size=16)
      self.HIGHLIGHTED_COL='#3E4149'
      self.UNHIGHLIGHTED_COL='White'
      #list of buttons for letters,and the letters themselves
      self.buttons = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
      self.letters = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
      #get the dice potentials
      self.dice = BoggleDice()
      #Create interface
      #Create window+title
      self.screen=screen
      screen.title(TITLE)
      self.btn_shuffle = Button(screen,text='Shuffle Board',width=BTN_WIDTH*4,height=BTN_HEIGHT,font=LETTER_FONT)
      self.btn_shuffle.grid(row=0,column=0,columnspan=4)
      self.btn_shuffle.configure(command=self.shuffle_board)
      #Create the 'word' label
      self.label_word = Label(screen,text='',width=BTN_WIDTH*4,height=BTN_HEIGHT,font=LETTER_FONT)
      self.label_word.grid(row=1,column=0,columnspan=4)
      #Create the letter buttons (4x4 grid)
      for i in range(4):
        for j in range(4):
          self.buttons[i][j] = Button(screen,text='_',width=BTN_WIDTH,height=BTN_HEIGHT,font=LETTER_FONT)
          self.buttons[i][j].grid(row=i+2,column=j)
          self.buttons[i][j].configure(command=partial(self.letter_click,i,j))
        
  def letter_click(self,i,j):
    #Was this the last button clicked and is down?
    if i == self.last_i[-1] and j == self.last_j[-1] and self.buttons[i][j].cget('highlightbackground') == self.HIGHLIGHTED_COL:
      #so unighlight it
      #print('Valid last button - remove/unhighlight')
      self.buttons[i][j].configure(highlightbackground=self.UNHIGHLIGHTED_COL)
      self.last_i.pop()
      self.last_j.pop()
      self.word = self.word[:-1]
    #If it's clickable (unhighlighted) 
    elif self.buttons[i][j].cget('highlightbackground') == self.UNHIGHLIGHTED_COL:
      try:
        #If it's an adjacent square
        #Note commented line is non-diaganols
        #if ((abs(i-self.last_i[-1]) == 1 and abs(j-self.last_j[-1]) == 0)) or ((abs(i-self.last_i[-1]) == 0 and abs(j-self.last_j[-1]) == 1)):
        if abs(i-self.last_i[-1]) == 1 or abs(j-self.last_j[-1]) == 1:
          ##print("It didn't crash so not first, and is adjacent - so use it")
          raise Exception()
        else:
          pass
          #print('Invalid - not adjacent')
      except:
        #Either raised an error by being first square, or forced by being adjacent
        #print('Valid *next* button - add and highlight')
        self.buttons[i][j].configure(highlightbackground=self.HIGHLIGHTED_COL)
        #print('updating last')
        self.last_i.append(i)
        self.last_j.append(j)
        self.word += self.letters[i][j]
        self.label_word.configure(text=self.word)
    else:
      #print('unclickable')
      pass
    print('Word:',self.word)

  def shuffle_board(self):
    for i in range(4):
      for j in range(4):
        self.letters[i][j] = self.dice.getLetter(i,j)
        self.buttons[i][j].configure(text=self.letters[i][j])
    print(self.letters)
