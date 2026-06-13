class RegistraAtletaError(ValueError):
    def __init__(self, messaggio, campo_errato):
        super().__init__(messaggio)
        self.campo_errato = campo_errato