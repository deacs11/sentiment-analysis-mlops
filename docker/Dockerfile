# Usa un'immagine Python ufficiale e leggera come base
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia prima il file dei requisiti per sfruttare la cache di Docker
COPY app/requirements.txt .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# --- MODIFICA CHIAVE ---
# Copia la cartella dei test dentro l'immagine
COPY tests/ ./tests/ 

# Copia tutto il resto del codice dell'applicazione nella directory di lavoro
# Assicurati che questa riga sia DOPO la copia dei test per coerenza
COPY app/ .

# Esponi la porta 5000, su cui Flask sarà in ascolto
EXPOSE 5000

# Definisci il comando per avviare l'applicazione.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]