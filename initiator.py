from tkinter import *
import os

root = Tk()
termf = Frame(root, height=400, width=500)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
#width=termf.winfo_width()
#print(width)
os.system('xterm -into %d -geometry 90x90 -sb &' % wid)

root.mainloop()
