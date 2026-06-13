from AppGUI import appGUI
import tkinter as tk
import BaseController as bc
import CompetitionController as cc

from Storage import Storage

storage = Storage()
storage.carica_atleti()
storage.carica_skill()
baseController = bc.BaseController(storage)
competitionController = cc.CompetitionController(storage)
root = tk.Tk()
app = appGUI(root, baseController, competitionController)
root.mainloop()
