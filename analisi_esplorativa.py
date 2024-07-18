import pandas as pd

class AnalisiEsplorativa:
    def __init__(self, dati):
        self.dati = dati
        
    def crea_colonne_utili(self):
        self.dati['Costo_per_GB'] = self.dati['Tariffa_Mensile'] / self.dati['Dati_Consumati']