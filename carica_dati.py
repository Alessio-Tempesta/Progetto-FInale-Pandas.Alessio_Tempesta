# Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
# telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
# vari attributi del cliente e la loro fedeltà.

# Dataset: 
# ID_Cliente: Identificativo unico per ogni cliente
# Età: Età del cliente
# Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
# Tariffa_Mensile: Quanto il cliente paga al mese
# Dati_Consumati: GB di dati consumati al mese
# Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
# Churn: Se il cliente ha lasciato la compagnia (Sì/No)

# Caricamento e Esplorazione Iniziale:
# Caricare i dati da un file CSV.
# Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
# valori mancanti.
# Pulizia dei Dati:
# Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
# Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
# Analisi Esplorativa dei Dati (EDA):
# Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
# Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
# Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
# Preparazione dei Dati per la Modellazione:
# Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
# Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
# Analisi Statistica e Predittiva:
# Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
# su altri fattori.
# Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).


import pandas as pd

# classe caricamento dati
class CaricatoreDati:
    def __init__(self, percorso_file ='file.csv'):
        self.percorso_file = percorso_file
        self.dati = None
        
    def carica_dati(self):
        # carichaimo i dati dal file csv
        try:
            self.dati = pd.read_csv(self.percorso_file)
            print(f"Dati sono stati caricati con successo da {self.percorso_file}")
            return self.dati
        except FileNotFoundError:
            print(f"Errore il file {self.percorso_file} non è stato trovato")
        
    #esplora i dati stampando info di base 
    def esplora_dati(self):
        if self.dati is not None:
            print("\nInformazioni sui dati:", self.dati.info())
            print("\n Statistiche descirttive: ")
            print(self.dati.describe())
            print("\nConteggio dei valori nella colonna 'Churn':")
            print(self.dati['Churn'].value_counts())
        else:
            print("I dati non sono stati ancora caricati.")

    def ottieni_dati(self):
        return self.dati
        