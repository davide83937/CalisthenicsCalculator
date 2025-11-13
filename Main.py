from AppGUI import appGUI
import tkinter as tk
import Caliculator as cc

root = tk.Tk()
app = appGUI(root)
cal = cc.Caliculator(app)
print("Carico")
cal.carica_atleti()
cal.carica_skill()
print("Caricato")


root.mainloop()

