import schedule
import time
import subprocess
from datetime import datetime
import os

# 📦 Liste des programmes à mettre à jour
PROGRAMMES = [
    "Google.Chrome",
    "Microsoft.VisualStudioCode",
    "Python.Python.3.12",
    "Postman.Postman",
    "Mozilla.Firefox"
]

# 📁 Dossier où seront stockés les fichiers logs
LOG_FOLDER = "logs"


def update_selected_programs():
    os.makedirs(LOG_FOLDER, exist_ok=True)

    log_filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M.txt")
    log_path = os.path.join(LOG_FOLDER, log_filename)

    def log(text):
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(text + "\n")

    start = datetime.now()
    log("============================================")
    log(f"🕘 Début de l'exécution : {start}")
    log("============================================\n")

    log("📦 Programmes à mettre à jour :")
    for p in PROGRAMMES:
        log(f" - {p}")
    log("")

    for prog in PROGRAMMES:
        log(f"🔄 Mise à jour de : {prog}")
        try:
            result = subprocess.run(
                ["winget", "upgrade", prog, "--silent"],
                capture_output=True,
                text=True
            )

            if result.stdout.strip():
                log("✔️ SORTIE :")
                log(result.stdout.strip())

            if result.stderr.strip():
                log("❌ ERREUR :")
                log(result.stderr.strip())

        except Exception as e:
            log(f"❌ Exception Python : {e}")

        log("--------------------------------------------")

    end = datetime.now()
    log(f"\n🕛 Fin de l'exécution : {end}")
    log(f"⏳ Durée totale : {end - start}")
    log("============================================\n")

    print(f"📁 Log généré : {log_path}")


# ⏰ Planification quotidienne à 6h du matin
schedule.every().day.at("15:00").do(update_selected_programs)

print("⏳ En attente… Le script exécutera les mises à jour chaque jour à 15:00.")

# 🔁 Boucle infinie
while True:
    schedule.run_pending()
    time.sleep(1)
