from AppGUI import appGUI
import tkinter as tk
import Caliculator as cc

# 1. PRIMA DI TUTTO: Creiamo il Singleton della logica di dominio.
# Questo fa sì che cc.Caliculator._instance non sia più None!
cal = cc.Caliculator()

# 2. Carichiamo i dati in memoria (il "motore" ora ha i dati)
cal.carica_atleti()
cal.carica_skill()

# 3. SOLO ORA avviamo l'interfaccia grafica.
# Quando la GUI nel suo __init__ chiamerà showAthletesZero(),
# la calcolatrice sarà pronta e piena di dati!
root = tk.Tk()
app = appGUI(root)

# (Se il ciclo for di cui parlavamo prima l'hai messo in showAthletesZero
# dentro la GUI, allora non serve metterlo anche qui nel Main.py)

# 4. Avviamo la finestra
root.mainloop()
