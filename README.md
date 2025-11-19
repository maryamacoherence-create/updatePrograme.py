📘 Documentation — Script de Mise à Jour Automatique des Programmes (via Winget)
🎯 Objectif du Script

Ce script Python permet de :

Vérifier chaque jour si certains logiciels installés sur l’ordinateur ont des mises à jour disponibles.

Lancer automatiquement leur mise à jour via Windows Package Manager (winget).

Générer un fichier log détaillé (date, heure, programmes mis à jour, erreurs éventuelles).

Fonctionner automatiquement chaque jour à 15h00 grâce à une planification (schedule).

C’est donc un outil d’automatisation de maintenance logicielle.

📂 Structure générale

Le script comporte :

Une liste de programmes à mettre à jour

Un système de logs enregistrant toutes les actions

Une fonction d’exécution des mises à jour

Une tâche planifiée qui s’exécute chaque jour

Une boucle infinie permettant au programme de rester actif



============================================
🕘 Début de l'exécution : 2025-01-19 15:00:01
============================================

📦 Programmes à mettre à jour :
 - Google.Chrome
 - Microsoft.VisualStudioCode
 - Python.Python.3.12
 - Postman.Postman
 - Mozilla.Firefox

🔄 Mise à jour de : Google.Chrome
✔️ SORTIE :
Found Google Chrome [Google.Chrome]
Updating...
Successfully updated

--------------------------------------------
...
🕛 Fin de l'exécution : 2025-01-19 15:02:10
⏳ Durée totale : 0:02:09
============================================
