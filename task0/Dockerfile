# Utilise l'image Ubuntu la plus récente comme base
FROM ubuntu:latest

# Met à jour la liste des paquets disponibles
RUN apt-get update

# Met à niveau tous les paquets installés (-y pour répondre "oui" automatiquement)
RUN apt-get upgrade -y

# Commande par défaut qui s'exécute quand le conteneur démarre
CMD echo "Hello, World!"