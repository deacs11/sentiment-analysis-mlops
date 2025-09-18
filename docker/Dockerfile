 # Usa un'immagine Python ufficiale e leggera come base
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia prima il file dei requisiti per sfruttare la cache di Docker
COPY app/requirements.txt .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del codice dell'applicazione nella directory di lavoro
COPY ./app .

# Esponi la porta 5000, su cui Flask sarà in ascolto
EXPOSE 5000

# Definisci il comando per avviare l'applicazione quando il container parte.
# Usiamo Gunicorn, un server WSGI robusto per la produzione, invece del server di sviluppo di Flask.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
