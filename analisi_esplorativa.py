import pandas as pd

class AnalisiEsplorativa:
    def __init__(self, dati):
        self.dati = dati
        
    # funzione che ci permette di creare nuove colonne utili per l'analisi
    def crea_colonne_utili(self):
        self.dati['Costo_per_GB'] = self.dati['Tariffa_Mensile'] / self.dati['Dati_Consumati']
        return self.dati
    
    # esplora le relazioni tra le variabili e churn
    def esplora_relazioni(self):
        print(self.dati.groupby('Churn')[['Età', 'Durata_Abonnamento', 'Tariffa_Mensile', 'Costo_per_GB']].mean())
        