# SQL Injection Tester

## Description

Ce script Python est conçu pour détecter les vulnérabilités d'injection SQL sur une URL cible. En utilisant une liste exhaustive de payloads SQL, le script envoie des requêtes HTTP à l'URL spécifiée avec différentes variations de payloads, puis analyse les réponses pour détecter toute indication d'une injection SQL.

## Fonctionnalités

- Détection des vulnérabilités d'injection SQL en envoyant des requêtes HTTP avec des payloads SQL variés.
- Analyse des réponses pour détecter les signes d'une injection SQL.
- Prise en charge de la gestion des sessions HTTP pour une exécution efficace des tests.
- Fonctionnalité d'arrêt manuel du script si aucune vulnérabilité n'est détectée après un certain temps.

## Installation

Clonez le repository et installez les dépendances requises :

```bash
git clone https://github.com/fzazking/sql_injection_tester.py
cd SQL-Injection-Tester
pip install -r requirements.txt
```
Lancez le script en fournissant l'URL cible à tester :
```bash
python sql_injection_tester.py
```
Entrez l'URL cible lorsque vous y êtes invité.

----------------------------------------------

## Contribuer

Les contributions sont les bienvenues ! Forkez ce repository, créez une branche, effectuez vos modifications et soumettez une pull request.

