import tkinter as tk
from cProfile import label
from tkinter import ttk
import copy

from Tools.scripts.win_add2path import modify


class appGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Caliculator")
        self.root.geometry("1920x1080")
        # Frame principale
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(expand=True, fill="both")
        self.but_reg = self.add_button("Registra nuovo atleta", command=self.openSubWindow)
        self.scroll = ttk.Scrollbar(self.main_frame)
        self.mylist = tk.Listbox(self.main_frame, yscrollcommand=self.scroll.set)
        self.but_reg.grid(row=0, column=0)
        self.scroll.grid(row =1, column=1, sticky="NS")
        self.mylist.grid(row=1, column=0, ipadx=200, ipady=400)
        self.nome_entry = None
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Errore.TEntry", fieldbackground="red")
        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Ok.TEntry", fieldbackground="green")
        self.style3 = ttk.Style()
        self.style3.theme_use('clam')
        self.style3.configure("white.TEntry", fieldbackground="white")
        self.modify = None
        self.save_button = None
        self.indexSetLine = 0



    def modify_button(self):
        self.nome_entry.config(style="white.TEntry", state="normal")
        self.cognome_entry.configure(style="white.TEntry", state="normal")
        self.età_entry.configure(style="white.TEntry", state="normal")
        self.codice_fiscale_entry.configure(style="white.TEntry", state="normal")
        self.cellulare_entry.configure(style="white.TEntry", state="normal")
        self.altezza_entry.configure(style="white.TEntry", state="normal")
        self.peso_entry.configure(style="white.TEntry", state="normal")
        self.email_entry.configure(style="white.TEntry", state="normal")
        self.modify.grid_remove()
        self.save_button.grid_remove()


    def save_button_f(self):
        import Caliculator as cc
        #print("save gui")
        cc.Caliculator.terminaRegistrazione(cc.Caliculator._instance)

    # Metodo per aggiungere pulsanti dinamicamente
    def add_button(self, text, command):
        btn = ttk.Button(self.main_frame, text=text, command=command)
        #btn.pack(pady=5)
        return btn


    def add_line(self, code, nome, cognome):
        line = tk.Frame(self.mylist)
        line.pack(fill="x", pady=2)
        self.code_label = tk.Label(line, text=code)
        self.code_label.grid(row=0, column=0)
        nome_label = tk.Label(line, text=nome)
        nome_label.grid(row=0, column=1)
        cognome_label = tk.Label(line, text=cognome)
        cognome_label.grid(row=0, column=2)
        button_add = tk.Button(line, text="Valuta", command=lambda:self.openEvaluationWindow(code))
        button_add.grid(row=0,column=3)



    def read_data(self, nome, cognome, età, c_fiscale, n_cellulare, altezza, peso, email):
        import Caliculator as cc
        nome = nome.get()
        cognome = cognome.get()
        età = int(età.get())
        c_fiscale = c_fiscale.get()
        n_cellulare = n_cellulare.get()
        altezza = float(altezza.get())
        peso = float(peso.get())
        email = email.get()
        result = cc.Caliculator.inserisciDati(cc.Caliculator._instance, nome, cognome, età, c_fiscale, n_cellulare, email, altezza, peso)
        print(result)
        if result == 1:
            self.nome_entry.config(style="Errore.TEntry")
        elif result == 2:
            self.cognome_entry.configure(style="Errore.TEntry")
        elif result == 3:
            self.età_entry.configure(style="Errore.TEntry")
        elif result == 4:
            self.codice_fiscale_entry.configure(style="Errore.TEntry")
        elif result == 5:
            self.cellulare_entry.configure(style="Errore.TEntry")
        elif result == 6:
            self.email_entry.configure(style="Errore.TEntry")
        elif result == 7:
            self.altezza_entry.configure(style="Errore.TEntry")
        elif result == 8:
            self.peso_entry.configure(style="Errore.TEntry")
        elif result == 0:
            self.nome_entry.config(style="Ok.TEntry", state="readonly")
            self.cognome_entry.configure(style="Ok.TEntry", state="readonly")
            self.età_entry.configure(style="Ok.TEntry", state="readonly")
            self.codice_fiscale_entry.configure(style="Ok.TEntry", state="readonly")
            self.cellulare_entry.configure(style="Ok.TEntry", state="readonly")
            self.altezza_entry.configure(style="Ok.TEntry", state="readonly")
            self.peso_entry.configure(style="Ok.TEntry", state="readonly")
            self.email_entry.configure(style="Ok.TEntry", state="readonly")
            self.modify.grid()
            self.save_button.grid()




    def openSubWindow(self):
        registerWindow = tk.Toplevel(self.root)
        registerWindow.title("Registra Nuovo Atleta")
        registerWindow.geometry("480x540")
        nome_label = ttk.Label(registerWindow, text="Nome")
        self.nome_entry = ttk.Entry(registerWindow)
        cognome_label = ttk.Label(registerWindow, text="Cognome")
        self.cognome_entry = ttk.Entry(registerWindow)
        età_label = ttk.Label(registerWindow, text="Età")
        self.età_entry = ttk.Entry(registerWindow)
        codice_fiscale_label = ttk.Label(registerWindow, text="Codice Fiscale")
        self.codice_fiscale_entry = ttk.Entry(registerWindow)
        cellulare_label = ttk.Label(registerWindow, text="Numero di Cellulare")
        self.cellulare_entry = ttk.Entry(registerWindow)
        altezza_label = ttk.Label(registerWindow, text="Altezza")
        self.altezza_entry = ttk.Entry(registerWindow)
        peso_label = ttk.Label(registerWindow, text="Peso")
        self.peso_entry = ttk.Entry(registerWindow)
        email_label = ttk.Label(registerWindow, text="Email")
        self.email_entry = ttk.Entry(registerWindow)
        self.modify = ttk.Button(registerWindow, text="Modifica", command=self.modify_button)
        conferma_button = ttk.Button(registerWindow, text="Conferma", command=lambda: self.read_data(self.nome_entry, self.cognome_entry, self.età_entry, self.codice_fiscale_entry,                                                                               self.cellulare_entry, self.altezza_entry, self.peso_entry, self.email_entry))
        self.save_button = ttk.Button(registerWindow, text="Salva", command=self.save_button_f)
        nome_label.grid(row=0, column=0)
        cognome_label.grid(row=0, column=1)
        self.nome_entry.grid(row=1, column=0)
        self.cognome_entry.grid(row=1, column=1)
        età_label.grid(row=4, column=2)
        self.età_entry.grid(row=5, column=2)
        email_label.grid(row=2, column=0)
        self.email_entry.grid(row=3, column=0)
        codice_fiscale_label.grid(row=2, column=1)
        self.codice_fiscale_entry.grid(row=3, column=1)
        cellulare_label.grid(row=2, column=2)
        self.cellulare_entry.grid(row=3, column=2)
        altezza_label.grid(row=4, column=0)
        self.altezza_entry.grid(row=5, column=0)
        peso_label.grid(row=4, column=1)
        self.peso_entry.grid(row=5, column=1)
        self.modify.grid(row=6, column=0)
        conferma_button.grid(row=6, column=1)
        self.save_button.grid(row=6, column=2)
        self.modify.grid_remove()
        self.save_button.grid_remove()

    def openEvaluationWindow(self, code):
        import Caliculator as cc
        self.evaluationWindow = tk.Toplevel(self.root)
        self.evaluationWindow.title("Valuta atleta")
        self.evaluationWindow.geometry("720x540")
        self.evaluationWindow.resizable(False, False)
        # Importante: grid_propagate va messo DOPO aver definito la geometry
        self.evaluationWindow.grid_propagate(False)

        cc.Caliculator.valutaAtleta(cc.Caliculator._instance, code)

        # Label del Codice Atleta
        self.code = ttk.Label(self.evaluationWindow, text=f"Atleta: {code}")
        self.code.grid(row=0, column=0, columnspan=2, pady=5)

        # 1. Configurazione CANVAS e SCROLLBAR
        self.canvas = tk.Canvas(self.evaluationWindow, width=450, height=350)  # Altezza fissa
        self.scrollSetLines = ttk.Scrollbar(self.evaluationWindow, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollSetLines.set)

        # Posizionamento Canvas (Colonna 0)
        self.canvas.grid(row=1, column=0, padx=10, pady=10)
        self.scrollSetLines.grid(row=1, column=1, sticky="ns")

        # 2. Sezione Input Bonus (Sotto il canvas)
        bonus_frame = ttk.Frame(self.evaluationWindow)
        bonus_frame.grid(row=2, column=0, pady=10)

        bonus_combo_label = ttk.Label(bonus_frame, text="Bonus Combo:")
        bonus_combo_label.grid(row=0, column=0, padx=5)

        bonus_combo_entry = ttk.Entry(bonus_frame, width=5)
        bonus_combo_entry.insert(0, "0")
        bonus_combo_entry.grid(row=0, column=1)

        # 3. Sezione Pulsanti Azione (Colonna 2)
        buttons_frame = ttk.Frame(self.evaluationWindow)
        buttons_frame.grid(row=1, column=2, padx=20, sticky="n")

        addSetLineButton = ttk.Button(buttons_frame, text="Aggiungi Linea", command=self.addSetLine)
        addSetLineButton.pack(pady=10)

        confermaButton = ttk.Button(buttons_frame, text="Conferma",
                                    command=lambda: self.calcolaPunteggio(addSetLineButton, confermaButton,
                                                                          int(bonus_combo_entry.get())))
        confermaButton.pack(pady=10)

        self.labelResult = ttk.Label(buttons_frame, text="", font=('Helvetica', 12, 'bold'))
        self.labelResult.pack(pady=20)

        # Inizializza la prima riga
        self.addSetLine()

    """def openEvaluationWindow(self, code):
        import Caliculator as cc
        self.evaluationWindow = tk.Toplevel(self.root)
        self.evaluationWindow.title("Valuta atleta")
        self.evaluationWindow.geometry("720x540")
        self.evaluationWindow.resizable(False, False)  # Impedisce all'utente di ridimensionare
        self.evaluationWindow.grid_propagate(False)  # Impedisce al contenuto di allargare la finestra
        cc.Caliculator.valutaAtleta(cc.Caliculator._instance, code)
        self.code = ttk.Label(self.evaluationWindow, text=code)
        self.scrollSetLines = ttk.Scrollbar(self.evaluationWindow)
        self.mySetLinesList = tk.Listbox(self.evaluationWindow, yscrollcommand=self.scrollSetLines.set)
        self.code.grid(row=0,column=1)
        self.scrollSetLines.grid(row=1, column=1, sticky="NS")
        self.mySetLinesList.grid(row=1, column=0, ipadx=100, ipady=150)
        bonus_combo_label = ttk.Label(self.evaluationWindow, text="BonusCombo")
        bonus_combo_entry = ttk.Entry(self.evaluationWindow)
        bonus_combo_entry.insert(0, "0")

        addSetLineButton =  ttk.Button(self.evaluationWindow, text="Aggiungi Linea", command=self.addSetLine)
        addSetLineButton.grid(row=0, column=2)
        confermaButton = ttk.Button(self.evaluationWindow, text="Conferma",
                                    command=lambda:
                                    self.calcolaPunteggio(addSetLineButton, confermaButton, int(bonus_combo_entry.get())))
        confermaButton.grid(row=0, column=3)
        self.labelResult = ttk.Label(self.evaluationWindow, text="")
        self.labelResult.grid(row=1, column=2)
        bonus_combo_label.grid(row=2, column=0)
        bonus_combo_entry.grid(row=3, column=0)
        self.addSetLine()"""



    def addSetLine(self):
        import Caliculator as cc
        #setLine = tk.Frame(self.mySetLinesList)
        setLine = tk.Frame(self.scrollable_frame)
        setLine.pack(fill="x", pady=2)
        scelta = tk.StringVar(value="Seleziona una skill")
        listaSkill = cc.Caliculator.getSkillList(cc.Caliculator._instance)
        tendinaSkill = ttk.OptionMenu(setLine, scelta, *(["Seleziona Skill"]+[s.nome for s in listaSkill]))
        tendinaSkill.grid(row=1, column=0)

        listaMalus = ["Seleziona Malus", 0, 0.1, 0.25, 0.5]
        sceltaMalus = tk.StringVar(value=str(listaMalus[0]))
        tendinaMalus = ttk.OptionMenu(setLine, sceltaMalus, *listaMalus)
        tendinaMalus.grid(row=1, column=1)
        confermaLineButton = ttk.Button(setLine, text="Conferma", command=lambda: self.confermaSingola(scelta, sceltaMalus, tendinaSkill, tendinaMalus, confermaLineButton))
        confermaLineButton.grid(row=1, column=2)
        self.indexSetLine = self.indexSetLine + 1


    def confermaSingola(self, skill, malus, tendinaSkill, tendinaMalus, lineButton):
        import Caliculator as cc
        tendinaSkill.configure(state="disabled")
        tendinaMalus.configure(state="disabled")
        lineButton.grid_remove()
        cc.Caliculator.inserisciSkillInSet(cc.Caliculator._instance, skill, float(malus.get()))



    def calcolaPunteggio(self, addLineButton, confermaButton, n_combo):
        import Caliculator as cc
        punteggio =cc.Caliculator.calcolaPunteggioSet(cc.Caliculator._instance, n_combo)
        self.labelResult.configure(text=punteggio)
        addLineButton.grid_remove()
        confermaButton.grid_remove()





