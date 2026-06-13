from AppGUI import appGUI
import tkinter as tk
import BaseController as bc
import CompetitionController as cc
#import Caliculator as cc

from Storage import Storage

storage = Storage()
storage.carica_atleti()
storage.carica_skill()
baseController = bc.BaseController()
competitionController = cc.CompetitionController()
root = tk.Tk()
app = appGUI(root)
root.mainloop()
