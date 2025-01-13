---

# SQL Injection Tester

## Description

Ce script Python est conçu pour détecter les vulnérabilités d'injection SQL sur une URL cible. Il envoie différentes requêtes HTTP avec des payloads SQL pour tester la présence de vulnérabilités dans les paramètres d'une page web. Le script vérifie si l'URL cible est vulnérable aux injections SQL en analysant les réponses.

### Fonctionnalités :
- Envoi de requêtes HTTP avec des payloads pour tester des injections SQL.
- Analyse de la réponse pour détecter des signes d'injections SQL.
- Utilisation de la bibliothèque **requests** pour effectuer les requêtes HTTP.

---

## Avertissement

⚠️ **Responsabilité :**

Ce script est uniquement destiné à des fins éducatives. **N'utilisez ce script que sur des sites pour lesquels vous avez l'autorisation explicite** d'effectuer des tests de sécurité. L'utilisation de ce script sur des systèmes sans autorisation explicite est **illégale** et peut entraîner des poursuites judiciaires. L'auteur de ce script ne pourra être tenu responsable des actions entreprises avec ce dernier.

### **N'utilisez ce script qu'avec l'autorisation explicite du propriétaire du site ou dans un environnement de test contrôlé.**

---

## Prérequis

Avant d'exécuter ce script, assurez-vous d'avoir installé Python 3 sur votre machine. Vous aurez également besoin de la bibliothèque **requests**.

### Installation de Python 3

Si vous n'avez pas Python 3 installé, vous pouvez le télécharger et l'installer depuis [le site officiel de Python](https://www.python.org/downloads/). Vous pouvez également installer Python via le gestionnaire de paquets de votre système :

#### Sur Ubuntu ou Kali Linux :
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Sur macOS (avec Homebrew) :
```bash
brew install python
```

#### Sur Windows :
1. Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).
2. Assurez-vous de cocher la case "Add Python to PATH" lors de l'installation.

---

## Utilisation

### Cloner le dépôt (Linux)

Si vous n'avez pas encore cloné le dépôt, vous pouvez le faire avec cette commande :

```bash
git clone https://github.com/fzazdbl/SQL-injection-tester
cd SQL-injection-tester
pip install -r requirements.txt
```

### Exécuter le script

1. Assurez-vous d'être dans le répertoire du projet où se trouve le fichier `sql_injection_tester.py`.
2. Utiliser un environnement virtuel (recommandé)
Pour éviter d'installer des paquets globalement et garder vos dépendances isolées, il est recommandé de créer un environnement virtuel.

Créer un environnement virtuel :
Dans l'invite de commandes, à partir du répertoire de votre projet, exécutez cette commande :

```bash
python -m venv venv
```

Activer l'environnement virtuel :
Pour activer l'environnement virtuel, exécutez cette commande dans l'invite de commandes :
```bash
.\venv\Scripts\activate
```

Vous verrez alors (venv) apparaître dans votre invite de commandes, ce qui signifie que l'environnement virtuel est activé.

Installer les dépendances :
Avec l'environnement virtuel activé, installez les dépendances nécessaires via le fichier requirements.txt:
```bash
pip install -r requirements.txt
```
Si vous ne souhaitez pas utiliser un environnement virtuel, vous pouvez simplement installer les dépendances globalement en exécutant:

```bash
pip install requests
```
### Exécuter le script
Pour exécuter le script, tapez simplement la commande suivante dans l'invite de commandes :

```bash
python sql_injection_tester.py
```
Le script vous demandera ensuite d'entrer l'URL de la cible que vous souhaitez tester. Par exemple :

```bash
Enter the target URL: http://example.com/page?id=1
```
Le script tentera alors de tester cette URL pour détecter des vulnérabilités d'injection SQL.
4. Exécutez le script Python avec la commande suivante :

```bash
python3 sql_injection_tester.py
```

3. Vous serez invité à entrer l'URL cible que vous souhaitez tester. Par exemple :

```bash
Enter the target URL: http://example.com/page?id=1
```
Le script testera l'URL pour détecter des vulnérabilités d'injection SQL et affichera les résultats dans la console.

---
Pour Windows 11/10
---
### Étape 1 : Télécharger le fichier ZIP
Comme nous allons éviter l'utilisation de Git, voici comment obtenir le dépôt :

1.Allez sur la page du projet sur GitHub : https://github.com/fzazdbl/SQL-injection-tester.
2.Cliquez sur le bouton "Code" et sélectionnez "Download ZIP".
3.Une fois le fichier ZIP téléchargé, extrayez-le dans un dossier de votre choix.
### Étape 2 : Installer les dépendances
Ouvrez une fenêtre d'invite de commandes (CMD) et accédez au dossier où vous avez extrait les fichiers.

Exemple :

```bash
cd C:\chemin\vers\SQL-injection-tester
```
Ensuite, installez les dépendances requises à l'aide de pip :

```bash
pip install -r requirements.txt
```
Cela installera les bibliothèques nécessaires, y compris requests.

### Étape 3 : Exécuter le script
Une fois les dépendances installées, vous pouvez exécuter le script Python en utilisant la commande suivante :

```bash
python sql_injection_tester.py
```

Le script vous demandera d'entrer l'URL de la cible que vous souhaitez tester. Par exemple :
```bash
Enter the target URL: http://example.com/page?id=1
```
Le script tentera alors de tester cette URL pour détecter des vulnérabilités d'injection SQL.

---

## Structure du projet

Voici la structure de votre projet :

```
/sql_injection_tester
│
├── sql_injection_tester.py    # Le script principal pour tester les injections SQL
├── requirements.txt           # Liste des dépendances Python
└── README.md                  # Ce fichier de documentation
```

---

## Licence

Ce projet est sous **licence MIT**. Vous pouvez consulter le fichier **LICENSE** pour plus de détails.

---

### Explication des commandes et des tests

- **`requests`** : Cette bibliothèque permet d'envoyer des requêtes HTTP, nécessaire pour interagir avec les sites web.
- Le script envoie des payloads SQL spécifiques dans l'URL et analyse les réponses pour rechercher des indices de vulnérabilités SQL.
- **`python3`** : Commande pour exécuter le script Python avec Python 3.

---
