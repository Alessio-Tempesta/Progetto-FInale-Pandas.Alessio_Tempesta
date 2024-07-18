#Punto 3 Analisi esplorativa dei Dati
# Creazione di nuove colonne e analisi di base:  Dipende dalla complessità delle nuove colonne da creare e delle relazioni da esplorare. tempo stimato 40-50 minuti.
# Calcolo delle correlazioni: 15-20 minuti per esaminare le correlazioni tra le variabili principali.

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
        
    # calcolo delle correlazioni tra le varibali

    def calcola_correlazioni(self):
        correlazioni = self.dati.corr()                                     #utilizzato per trovare la correlazione a coppie di tutte le colonne nel Pandas Dataframe in Python
        print(correlazioni)
        return correlazioni
