#Punto 4 Preparazione dei Dati per la Modellazione
# Conversione della colonna : Poche righe di codice, tempo stimato: 20 minuti.
# Normalizzazione delle colonne numeriche: circa 20-30 minuti.

import pandas as pd 
import numpy as np

class PreparazioneDati:
    def __init__(self, dati):
        self.dati = dati
    
    #Convertire la colonna 'Churn' in formato num
    def converti_churn(self):
        try:
            # Converte la colonna 'Churn' in formato numerico
            self.dati['Churn'] = self.dati['Churn'].apply(lambda x: 1 if x == 'Sì' else 0)
            print("Colonna 'Churn' convertita con successo.")
        except KeyError:
            print("Errore: la colonna 'Churn' non è presente nel dataset.")
        except Exception as e:
            print(f"Errore durante la conversione della colonna 'Churn': {e}")
        return self.dati
    
    # normalizza le colonne numeriche 
    def normalizza_colonne(self):
        colonne_da_normalizzare = ['Età', 'Durata_Abonnamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']
        try:
            # Normalizza le colonne numeriche per la modellazione
            self.dati[colonne_da_normalizzare] = (self.dati[colonne_da_normalizzare] - self.dati[colonne_da_normalizzare].mean()) / self.dati[colonne_da_normalizzare].std()
            print("Colonne normalizzate con successo.")
        except KeyError as e:
            print(f"Errore: una o più colonne non sono presenti nel dataset: {e}")
        except Exception as e:
            print(f"Errore durante la normalizzazione delle colonne: {e}")
        return self.dati
    
    