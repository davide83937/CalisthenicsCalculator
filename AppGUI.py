import tkinter as tk
from tkinter import ttk

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
        self.mylist.grid(row=1, column=0, ipadx=20, ipady=40)
        self.showAthletesZero()
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
        self.startCompetitionButton = self.add_button("StartCompetition", command=self.openCompetitionWindow)
        self.startCompetitionButton.grid(row=0, column=2)
        self.lista_partecipanti_temp = []

    def showAthletesZero(self):
        import Caliculator as cc
        mode = "general"
        for codice, atl in cc.Caliculator.getElencoAtleti(cc.Caliculator._instance).items():
             self.add_line(codice, atl.nome, atl.cognome, "valuta", mode, self.mylist)


    def showAthletes(self):
        import Caliculator as cc
        self.scroll2 = ttk.Scrollbar(self.main_frame)
        self.mylist2 = tk.Listbox(self.main_frame, yscrollcommand=self.scroll.set)
        self.scroll2.grid(row=1, column=3, sticky="NS")
        self.mylist2.grid(row=1, column=2, ipadx=20, ipady=40)
        mode = "classifica"
        for codice, atl in cc.Caliculator.getElencoAtleti(cc.Caliculator._instance).items():
            if codice in self.lista_partecipanti_temp:
                self.add_line(codice, atl.nome, atl.cognome, "valuta", mode, self.mylist2)
        self.makeClassificationButton = self.add_button("Genera Classifica", command=self.generaClassifica)
        self.makeClassificationButton.grid(row=1, column=4)



    def generaClassifica(self):
        import Caliculator as cc
        comp = cc.Caliculator.getCompetizioneAttuale(cc.Caliculator._instance)
        classificaOrdinata = comp.getClassificaOrdinata()
        if classificaOrdinata is None:
            return
        # 1. Mostra le intestazioni
        self.showClassification()
        # 2. Riempie la classifica con i dati
        self.makeClassification(classificaOrdinata)

    def showClassification(self):
        # Se la classifica esiste già a schermo, la distruggiamo per svuotarla
        # (Questo risolve il bug degli atleti duplicati sulla GUI se premi due volte!)
        if hasattr(self, 'classifica_frame') and self.classifica_frame is not None:
            self.classifica_frame.destroy()

        # Creiamo un frame "contenitore" solo per la classifica
        self.classifica_frame = ttk.Frame(self.main_frame)
        # Lo mettiamo a destra di tutto (column=5), allineato in alto (sticky="n")
        self.classifica_frame.grid(row=1, column=5, sticky="n", padx=30)

        # Usiamo riga 0 e 1 DEL FRAME, quindi non interferiscono con il resto della GUI
        tk.Label(self.classifica_frame, text="CLASSIFICA", font=('Helvetica', 12, 'bold')).grid(row=0, column=0,
                                                                                                columnspan=5, pady=10)

        tk.Label(self.classifica_frame, text="Pos").grid(row=1, column=0, padx=5)
        tk.Label(self.classifica_frame, text="Nome").grid(row=1, column=1, padx=5)
        tk.Label(self.classifica_frame, text="Cognome").grid(row=1, column=2, padx=5)
        tk.Label(self.classifica_frame, text="Punti").grid(row=1, column=3, padx=5)
        tk.Label(self.classifica_frame, text="Cod").grid(row=1, column=4, padx=5)

    def makeClassification(self, classificaOrdinata):
        import Caliculator as cc
        row = 2
        lista_atleti = cc.Caliculator.getElencoAtleti(cc.Caliculator._instance)
        for co in classificaOrdinata:
            atleta = lista_atleti[co[0]]
            self.makeClassificationItem(co[0], atleta.nome, atleta.cognome, co[1], co[2], row)
            row = row + 1

    def makeClassificationItem(self, code, nome, cognome, punteggio, posizione, row):
        # Anziché usare self.main_frame, inseriamo le etichette in self.classifica_frame
        tk.Label(self.classifica_frame, text=posizione).grid(row=row, column=0)
        tk.Label(self.classifica_frame, text=nome).grid(row=row, column=1)
        tk.Label(self.classifica_frame, text=cognome).grid(row=row, column=2)
        tk.Label(self.classifica_frame, text=punteggio).grid(row=row, column=3)
        tk.Label(self.classifica_frame, text=code).grid(row=row, column=4)



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
        atleta = cc.Caliculator.terminaRegistrazione(cc.Caliculator._instance)
        mode = "general"
        if atleta:
            self.add_line(atleta.codice, atleta.nome, atleta.cognome, "valuta", mode)

    # Metodo per aggiungere pulsanti dinamicamente
    def add_button(self, text, command):
        btn = ttk.Button(self.main_frame, text=text, command=command)
        return btn

    def add_athlete_temp(self, code):
        if code not in self.lista_partecipanti_temp:
            self.lista_partecipanti_temp.append(code)
            n = len(self.lista_partecipanti_temp)
            self.string.set("Numero di partecipanti = " + str(n))

    def add_line(self, code, nome, cognome, goal, mode,  myLista = None):
        if myLista == None:
            myLista = self.mylist
        if goal == "valuta":
            function = lambda:self.openEvaluationWindow(code, mode)
        elif goal == "partecipa":
            function = lambda: self.add_athlete_temp(code)
        line = tk.Frame(myLista)
        line.pack(fill="x", pady=2)
        self.code_label = tk.Label(line, text=code)
        self.code_label.grid(row=0, column=0)
        nome_label = tk.Label(line, text=nome)
        nome_label.grid(row=0, column=1)
        cognome_label = tk.Label(line, text=cognome)
        cognome_label.grid(row=0, column=2)
        button_add = tk.Button(line, text=goal, command=function)
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

    def openEvaluationWindow(self, code, mode):
        import Caliculator as cc
        self.evaluationWindow = tk.Toplevel(self.root)
        self.evaluationWindow.title("Valuta atleta")
        self.evaluationWindow.geometry("720x540")
        self.evaluationWindow.resizable(False, False)
        # Importante: grid_propagate va messo DOPO aver definito la geometry
        self.evaluationWindow.grid_propagate(False)
        cc.Caliculator.valutaAtleta(cc.Caliculator._instance, code)

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

        buttons_frame = ttk.Frame(self.evaluationWindow)
        buttons_frame.grid(row=1, column=2, padx=20, sticky="n")

        addSetLineButton = ttk.Button(buttons_frame, text="Aggiungi Linea", command=self.addSetLine)
        addSetLineButton.pack(pady=10)

        confermaButton = ttk.Button(buttons_frame, text="Conferma",
                                    command=lambda: self.calcolaPunteggio(addSetLineButton, confermaButton,
                                                                          int(bonus_combo_entry.get()),  mode))
        confermaButton.pack(pady=10)

        self.labelResult = ttk.Label(buttons_frame, text="", font=('Helvetica', 12, 'bold'))
        self.labelResult.pack(pady=20)

        # Inizializza la prima riga
        self.addSetLine()


    def openCompetitionWindow(self):
        import Caliculator as cc
        self.lista_partecipanti_temp = []
        self.competitionWindow = tk.Toplevel(self.root)
        self.competitionWindow.title("Valuta atleta")
        self.competitionWindow.geometry("720x850")
        self.scrollComp = ttk.Scrollbar(self.competitionWindow)
        self.mylistComp = tk.Listbox(self.competitionWindow, yscrollcommand=self.scrollComp.set)
        self.scrollComp.grid(row=1, column=1, sticky="NS")
        self.mylistComp.grid(row=1, column=0, ipadx=20, ipady=40)
        self.beginCompetitionButton = ttk.Button(self.competitionWindow, text="Inizio", command=lambda: self.startCompetition())
        self.beginCompetitionButton.grid(row=0, column=2)
        self.string = tk.StringVar()
        self.n_partecipanti = ttk.Label(self.competitionWindow, textvariable=self.string)
        n = len(self.lista_partecipanti_temp)
        self.string.set("Numero di partecipanti = "+str(n))
        self.n_partecipanti.grid(row=1, column=2)

        calcolatrice = cc.Caliculator()

        elenco_atleti = calcolatrice.getElencoAtleti()
        mode = "partecipa"
        for codice, atl in elenco_atleti.items():
            self.add_line(codice, atl.nome, atl.cognome, "partecipa", mode, self.mylistComp)



    def startCompetition(self):
        import Caliculator as cc
        cc.Caliculator.creaNuovaCompetizione(cc.Caliculator._instance, self.lista_partecipanti_temp)
        self.showAthletes()


    def addSetLine(self):
        import Caliculator as cc
        setLine = tk.Frame(self.scrollable_frame)
        setLine.pack(fill="x", pady=2)
        scelta = tk.StringVar(value="Seleziona una skill")
        listaSkill = cc.Caliculator.getSkillList(cc.Caliculator._instance)
        tendinaSkill = ttk.OptionMenu(setLine, scelta, *(["Seleziona Skill"]+[s.nome for s in listaSkill]))
        tendinaSkill.grid(row=1, column=0)
        sceltaMalus = tk.StringVar(value="Seleziona un malus")
        listaMalus = ["Seleziona Malus", 0, 0.1, 0.25, 0.5]
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



    def calcolaPunteggio(self, addLineButton, confermaButton, n_combo, mode):
        import Caliculator as cc
        punteggio =cc.Caliculator.calcolaPunteggioSet(cc.Caliculator._instance, n_combo, mode)
        self.labelResult.configure(text=punteggio)
        addLineButton.grid_remove()
        confermaButton.grid_remove()





