# Base Ubuntu
FROM ubuntu:latest

# Mise à jour des paquets
RUN apt-get update
RUN apt-get upgrade -y

# Installation de Python et pip
RUN apt-get install -y python3 python3-pip

# Solution au problème "externally-managed-environment"
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Installation de Flask
RUN pip3 install flask

# Installe le module CORS
RUN pip3 install flask-cors

# Définit /app comme répertoire de travail
WORKDIR /app

# Copie le fichier api.py dans l'image
COPY ./api.py /app/api.py

# Commande pour lancer l'application Flask
CMD ["python3", "api.py"]