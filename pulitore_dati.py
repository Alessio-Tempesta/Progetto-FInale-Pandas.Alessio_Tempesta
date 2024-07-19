# Punto 2 Pulizia dei Dati:
# -gestione dei valori mancanti : dipende dalla quantità di dati mancanti e dalla decisione di rimuovere o imputare valori ,correzione delle anomalie: Dipedne dalla natura delle anomalie  tempo stimato in totale = 45 minuti credo  

import pandas as pd

class PulitoreDati:
    def __init__(self, dati):
        self.dati = dati

    # Esegue tutte le operazioni di pulizia dei dati
    def pulisci_dati(self):
        self.gestisci_valori_mancanti()
        self.correggi_anomalie()
        return self.dati

    def gestisci_valori_mancanti(self):
        # Gestisce i valori mancanti rimuovendo le righe con NaN
        self.dati.dropna(inplace=True)

        # Corregge le anomalie nei dati, come età o tariffe negative.
    def correggi_anomalie(self):
        self.dati = self.dati[self.dati['Età'] > 0]
        self.dati = self.dati[self.dati['Tariffa_Mensile'] > 0]
        self.dati = self.dati[self.dati['Durata_Abonnamento'] > 0]
        self.dati = self.dati[self.dati['Dati_Consumati'] >= 0]
        