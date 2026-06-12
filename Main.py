from AppGUI import appGUI
import tkinter as tk
import Caliculator as cc


cal = cc.Caliculator()

cal.carica_atleti()
cal.carica_skill()
root = tk.Tk()
app = appGUI(root)


root.mainloop()

