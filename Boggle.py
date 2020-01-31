from tkinter import Tk,Label,font,Button,RAISED,SUNKEN

from BoggleBoard import BoggleBoard

import time

tk = Tk()
board = BoggleBoard(tk)
board.shuffle_board()
board.clock(tk)
tk.mainloop()