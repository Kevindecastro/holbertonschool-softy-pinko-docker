# Utilise l'image officielle Nginx
FROM nginx:latest

# Copie les fichiers du front-end dans le répertoire Nginx
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copie la configuration Nginx personnalisée
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf