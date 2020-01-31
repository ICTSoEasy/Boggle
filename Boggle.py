from tkinter import Tk,Label,font,Button,RAISED,SUNKEN

from BoggleBoard import BoggleBoard

tk = Tk()
board = BoggleBoard(tk)
board.shuffle_board()
tk.mainloop()