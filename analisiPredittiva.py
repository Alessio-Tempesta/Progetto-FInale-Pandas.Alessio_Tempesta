# Punto 5  Analisi Statistica e Predittiva
# Implementazione e addestramento del modello di regressione logistica: Dipende dalla complessità del modello e dalla dimensione del dataset, potrebbe richiedere 30-60 minuti.
# Valutazione del modello: 20-30 minuti per calcolare le metriche di valutazione come l'accuratezza e l'AUC.


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Creo classe modello
class ModelloPredittivo:
    def __init__(self, dati):
        self.dati = dati
        self.modello = None
        