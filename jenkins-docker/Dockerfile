# Partiamo dall'immagine ufficiale di Jenkins che hai usato
FROM jenkinsci/blueocean

# Passiamo all'utente root per poter installare software
USER root

# Installiamo il client Docker
RUN apt-get update && \
    apt-get install -y lsb-release && \
    curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc https://download.docker.com/linux/debian/gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce-cli

# Torniamo all'utente jenkins
USER jenkins