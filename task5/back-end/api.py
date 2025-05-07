from flask import Flask
from flask_cors import CORS  # Import pour gérer les requêtes cross-origin

# Crée une instance de l'application Flask
app = Flask(__name__)
CORS(app)  # Active CORS pour toutes les routes

# Définit une route qui retourne "Hello, World!"
@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

# Point d'entrée principal
if __name__ == '__main__':
    # Lance le serveur sur toutes les interfaces
    # (0.0.0.0) et port 5252
    app.run(host='0.0.0.0', port=5252)
