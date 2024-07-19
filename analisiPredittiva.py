# Punto 5  Analisi Statistica e Predittiva
# Implementazione e addestramento del modello di regressione logistica: Dipende dalla complessità del modello e dalla dimensione del dataset, potrebbe richiedere 30-60 minuti.
# Valutazione del modello: 20-30 minuti per calcolare le metriche di valutazione come l'accuratezza e l'AUC.


# Creo classe modello
class ModelloPredittivo:
    def __init__(self, dati):
        self.dati = dati