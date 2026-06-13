import tkinter as tk
from tkinter import ttk, messagebox




class appGUI:

    def __init__(self, root, baseController, competitionController):
        self.baseController = baseController
        self.competitionController = competitionController

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
        self.lista_partecipanti_temp = []
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


    def showAthletesZero(self):
        for codice, atl in self.baseController.getElencoAtleti().items():
             self.add_line(codice, atl.nome, atl.cognome, "valuta", "simple", self.mylist)


    def showAthletes(self):
        self.scroll2 = ttk.Scrollbar(self.main_frame)
        self.mylist2 = tk.Listbox(self.main_frame, yscrollcommand=self.scroll.set)
        self.scroll2.grid(row=1, column=3, sticky="NS")
        self.mylist2.grid(row=1, column=2, ipadx=20, ipady=40)

        for codice, atl in self.baseController.getElencoAtleti().items():
            if codice in self.lista_partecipanti_temp:
               self.add_line(codice, atl.nome, atl.cognome, "valuta", "competition", self.mylist2)
        self.makeClassificationButton = self.add_button("Genera Classifica", command=self.generaClassifica)
        self.makeClassificationButton.grid(row=1, column=4)



    def generaClassifica(self):

        classificaOrdinata = self.competitionController.generaClassifica()
        if classificaOrdinata is None:
            return
        # 1. Mostra le intestazioni
        self.showClassification()
        # 2. Riempie la classifica con i dati
        self.makeClassification(classificaOrdinata)
        self.mostraTabellone()

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
        row = 2
        lista_atleti = self.baseController.getElencoAtleti()
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
        atleta = self.baseController.terminaRegistrazione()
        if atleta:
            self.add_line(atleta.codice, atleta.nome, atleta.cognome, "valuta", "simple")

    # Metodo per aggiungere pulsanti dinamicamente
    def add_button(self, text, command):
        btn = ttk.Button(self.main_frame, text=text, command=command)
        return btn

    def add_athlete_temp(self, code):
        if code not in self.lista_partecipanti_temp:
            self.lista_partecipanti_temp.append(code)
            n = len(self.lista_partecipanti_temp)
            self.string.set("Numero di partecipanti = " + str(n))

    def add_line(self, code, nome, cognome, goal, mode, myLista = None):
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

        # --- MODIFICA QUI: Salva il pulsante se serve a valutare ---
        if goal == "valuta":
            if not hasattr(self, 'valuta_buttons'):
                self.valuta_buttons = {}
            self.valuta_buttons[code] = button_add
        # -----------------------------------------------------------



    def read_data(self, nome, cognome, età, c_fiscale, n_cellulare, altezza, peso, email):
        nome = nome.get()
        cognome = cognome.get()
        età = int(età.get())
        c_fiscale = c_fiscale.get()
        n_cellulare = n_cellulare.get()
        altezza = float(altezza.get())
        peso = float(peso.get())
        email = email.get()
        result = self.baseController.inserisciDati(nome, cognome, età, c_fiscale, n_cellulare, email, altezza, peso)
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

    def openEvaluationWindow(self, code, mode, index_match=1000):
        self.evaluationWindow = tk.Toplevel(self.root)
        self.evaluationWindow.title("Valuta atleta")
        self.evaluationWindow.geometry("720x540")
        self.evaluationWindow.resizable(False, False)
        # Importante: grid_propagate va messo DOPO aver definito la geometry
        self.evaluationWindow.grid_propagate(False)

        self.baseController.valutaAtleta(code)

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
                                                                          int(bonus_combo_entry.get()), index_match, code, mode))
        confermaButton.pack(pady=10)

        self.labelResult = ttk.Label(buttons_frame, text="", font=('Helvetica', 12, 'bold'))
        self.labelResult.pack(pady=20)

        # Inizializza la prima riga
        self.addSetLine()


    def openCompetitionWindow(self):
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

        elenco_atleti = self.baseController.getElencoAtleti()

        # 3. La GUI usa "se stessa" (self) per aggiornare la visualizzazione
        for codice, atl in elenco_atleti.items():
            self.add_line(codice, atl.nome, atl.cognome, "partecipa", "competition", self.mylistComp)

        # --- FINE PARTE REFACTORIZZATA ---


    def startCompetition(self):

        self.competitionController.creaNuovaCompetizione(self.lista_partecipanti_temp)
        self.showAthletes()


    def addSetLine(self):
        setLine = tk.Frame(self.scrollable_frame)
        setLine.pack(fill="x", pady=2)
        scelta = tk.StringVar(value="Seleziona una skill")
        listaSkill = self.baseController.getSkillList()
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
        tendinaSkill.configure(state="disabled")
        tendinaMalus.configure(state="disabled")
        lineButton.grid_remove()
        self.baseController.inserisciSkillInSet(skill, float(malus.get()))



    def calcolaPunteggio(self, addLineButton, confermaButton, n_combo, index, code, mode):
        finalSet = self.baseController.calcolaPunteggioSet(n_combo)
        self.labelResult.configure(text=finalSet.punteggio_totale)

        if mode == "competition":
            winner, stato = self.competitionController.registraSet(finalSet, code, index)
            addLineButton.grid_remove()
            confermaButton.grid_remove()
            # --- MODIFICA QUI: Cambia la grafica sulla linea dell'atleta nella lista principale ---
            if hasattr(self, 'valuta_buttons') and code in self.valuta_buttons:
                # hex #c3e6cb è un verde chiaro pastello molto pulito, #155724 è un testo verde scuro
                self.valuta_buttons[code].config(
                    text="Valutato ✔",
                    bg="#c3e6cb",
                    fg="#155724",
                    state="disabled"
                )
            # -------------------------------------------------------------------------------------
            if winner is not None:
                self.colora_match_concluso(index, winner)
                self.aggiornaTabellone(index, winner, stato)

    def inserisciSfidanti(self):
        index, first, second = self.competitionController.creaMatch()
        atl1 = first.Atleta
        atl2 = second.Atleta
        codAtl1 = atl1.codice
        codAtl2 = atl2.codice
        str1 = f"{atl1.nome} {atl1.cognome}"
        str2 = f"{atl2.nome} {atl2.cognome}"
        return index, str1, str2, codAtl1, codAtl2

    def riempiOttavi(self, n):
        sfidantiOttavi = []
        for i in range(0, n):
            index, str1, str2, cod1, cod2 = self.inserisciSfidanti()
            sfidantiOttavi.append((index, str1, str2, cod1, cod2))
        return sfidantiOttavi

   

    def aggiornaTabellone(self, current_match, vincitore, stato):
        if stato.is_finale():
            # Opzionale: Qui potresti lanciare un pop-up per festeggiare il vincitore del torneo!
            print(f"Torneo concluso! Ha vinto {vincitore.Atleta.nome} {vincitore.Atleta.cognome}")
            # --- LANCIO DEL POP-UP DI VITTORIA ---
            messagebox.showinfo(
                title="Torneo Concluso!",
                message=f"Il vincitore assoluto del torneo è {vincitore.Atleta.nome} {vincitore.Atleta.cognome}!\nCongratulazioni!"
            )
            return

        nome_completo_vincitore = f"{vincitore.Atleta.nome} {vincitore.Atleta.cognome}"
        codice_vincitore = vincitore.Atleta.codice
        next_match, fase, indice_fase, posizione = stato.get_destinazione_vincitore(current_match)

        chiave_ui = (fase, indice_fase, posizione)

        if chiave_ui in self.labels_tabellone:
            btn = self.labels_tabellone[chiave_ui]
            btn.config(text=nome_completo_vincitore)

            # Uso parametri di default nella lambda per legare i valori in modo sicuro
            btn.config(command=lambda c=codice_vincitore, m=next_match: self.openEvaluationWindow(c, "competition", m))

    def mostraTabellone(self):
        if hasattr(self, 'bracket_frame') and self.bracket_frame is not None:
            self.bracket_frame.destroy()

        self.bracket_frame = ttk.Frame(self.main_frame)
        self.bracket_frame.grid(row=1, column=6, sticky="n", padx=15)

        tk.Label(self.bracket_frame, text="TABELLONE 1v1", font=('Helvetica', 12, 'bold')).grid(row=0, column=0,
                                                                                                columnspan=4, pady=5)

        fasi = ["Ottavi", "Quarti", "Semifinali", "Finale"]
        for col, fase in enumerate(fasi):
            tk.Label(self.bracket_frame, text=fase, font=('Helvetica', 10, 'bold')).grid(row=1, column=col, pady=2)

        posizioni = {
            "Ottavi": [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)],
            "Quarti": [(2, 2), (4, 2), (6, 2), (8, 2)],
            "Semifinali": [(2, 4), (6, 4)],
            "Finale": [(2, 8)]
        }

        sfidanti_ottavi = self.riempiOttavi(8)

        # DIZIONARIO PER SALVARE I RIFERIMENTI GRAFICI delle Label
        self.labels_tabellone = {}

        for col, fase in enumerate(fasi):
            configurazioni = posizioni[fase]
            for i, (row, rowspan) in enumerate(configurazioni):
                if fase == "Ottavi":
                    index, nome1, nome2, cod1, cod2 = sfidanti_ottavi[i]
                else:
                    # Per i Quarti (i va da 0 a 3) -> index diventa da 1 a 4
                    # Per le Semifinali (i va da 0 a 1) -> index diventa 1 e 2
                    index = i + 1
                    nome1, nome2 = "TBD", "TBD"
                    cod1, cod2 = "TBD", "TBD"

                # Passiamo anche il parametro 'fase' a crea_match_box
                self.crea_match_box(self.bracket_frame, row, col, rowspan, nome1, nome2, index, cod1, cod2, fase)

    def crea_match_box(self, parent, row, col, rowspan, nome1, nome2, index, cod1, cod2, fase):
        # Ripristiniamo un leggero padding esterno ed interno per dare respiro
        box = tk.Frame(parent, borderwidth=1, relief="solid", bg="lightgrey", padx=2, pady=2)
        box.grid(row=row, column=col, rowspan=rowspan, padx=6, pady=3)

        # Font riportato a 9, larghezza a 13.
        # bd=2 ridà il classico effetto "pulsante" cliccabile 3D
        btn1 = tk.Button(box, text=nome1, width=13, font=('Helvetica', 9), cursor="hand2", bd=2)
        btn2 = tk.Button(box, text=nome2, width=13, font=('Helvetica', 9), cursor="hand2", bd=2)

        btn1.config(command=lambda b_win=btn1, b_lose=btn2: self.openEvaluationWindow(cod1, "competition", index))
        btn2.config(command=lambda b_win=btn2, b_lose=btn1: self.openEvaluationWindow(cod2, "competition", index))

        # Spazio di 1 pixel tra i due sfidanti nel box
        btn1.pack(pady=1)
        btn2.pack(pady=1)

        # SALVATAGGIO DEI RIFERIMENTI NEL DIZIONARIO
        # Inizializziamo il dizionario come rete di sicurezza nel caso non lo avessi fatto altrove
        if not hasattr(self, 'labels_tabellone'):
            self.labels_tabellone = {}

        # Memorizziamo il bottone 1 e il bottone 2 usando la chiave univoca (Fase, Indice, Sfidante 1 o 2)
        self.labels_tabellone[(fase, index, 1)] = btn1
        self.labels_tabellone[(fase, index, 2)] = btn2

    def imposta_vincitore(self, btn_vincente, btn_perdente):
        btn_vincente.config(bg="green", fg="white", state="disabled")
        btn_perdente.config(bg="red", fg="white", state="disabled")

    def colora_match_concluso(self, current_match, vincitore):
        # 1. Determina la fase e l'indice del match APPENA CONCLUSO
        if 1 <= current_match <= 8:
            fase = "Ottavi"
            indice_fase = current_match
        elif 9 <= current_match <= 12:
            fase = "Quarti"
            indice_fase = current_match - 8
        elif 13 <= current_match <= 14:
            fase = "Semifinali"
            indice_fase = current_match - 12
        elif current_match == 15:
            fase = "Finale"
            indice_fase = 1
        else:
            return

        # 2. Costruisci le chiavi per trovare i due bottoni di questo match
        chiave_btn1 = (fase, indice_fase, 1)
        chiave_btn2 = (fase, indice_fase, 2)

        if chiave_btn1 in self.labels_tabellone and chiave_btn2 in self.labels_tabellone:
            btn1 = self.labels_tabellone[chiave_btn1]
            btn2 = self.labels_tabellone[chiave_btn2]

            # MODIFICA: Usa la stringa Nome + Cognome per il confronto
            nome_completo_vincente = f"{vincitore.Atleta.nome} {vincitore.Atleta.cognome}"

            # 3. Controlla il testo sui bottoni e applica i colori
            if btn1.cget("text") == nome_completo_vincente:
                self.imposta_vincitore(btn1, btn2)
            elif btn2.cget("text") == nome_completo_vincente:
                self.imposta_vincitore(btn2, btn1)

