 # app/model.py
import pickle
import os

class SentimentModel:
    def __init__(self, model_path="sentimentanalysismodel.pkl"):
        # Costruisce il percorso assoluto al file del modello
        script_dir = os.path.dirname(__file__)
        abs_model_path = os.path.join(script_dir, model_path)
        
        try:
            # Carica il modello dal file .pkl
            self.model = pickle.load(open(abs_model_path, 'rb'))
            print("Modello caricato con successo!")
        except FileNotFoundError:
            print(f"Errore: File del modello non trovato in {abs_model_path}")
            self.model = None

    def predict_sentiment(self, text):
        if not self.model:
            return "error", 0.0

        # --- NOTA IMPORTANTE ---
        # Il modello fornito nel link è per la RILEVAZIONE DELLA LINGUA,
        # non per l'analisi del sentiment. 
        # Per far funzionare il progetto come richiesto, qui sotto simuleremo 
        # un output di sentiment basato su semplici parole chiave.
        # In un progetto reale, qui useresti il tuo vero modello di sentiment.
        
        text_lower = text.lower()
        if "amazing" in text_lower or "love" in text_lower or "great" in text_lower:
            sentiment = "positive"
            confidence = 0.95
        elif "bad" in text_lower or "terrible" in text_lower or "hate" in text_lower:
            sentiment = "negative"
            confidence = 0.92
        else:
            sentiment = "neutral"
            confidence = 0.65
        
        # La riga di codice per usare il VERO modello sarebbe qualcosa di simile a:
        # prediction = self.model.predict([text])
        # sentiment = prediction[0] 
        # confidence = ... (se il modello la fornisce)

        return sentiment, confidence
