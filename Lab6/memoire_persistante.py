import json, os, re

FICHIER = "memory.json"

# Charger ou créer la mémoire
if os.path.exists(FICHIER):
    with open(FICHIER, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

msg = input("Vous : ").lower()

# Enregistrer le nom
if "je m'appelle" in msg:
    memory["nom"] = msg.split()[-1]
    print(f"Enchanté {memory['nom']}, je m'en souviendrai.")

# Enregistrer le sport
elif "j'aime" in msg or "j’aime" in msg:
    sport = re.sub(r"j['’]aime\s+(le|la|les)?\s*", "", msg).strip()
    memory["sport"] = sport
    print(f"Tu aimes {sport}, je m'en souviendrai.")

# Rappeler les infos
elif "nom" in msg:
    print(f"Tu t'appelles {memory.get('nom','(inconnu)')}.")
elif "sport" in msg:
    print(f"Ton sport préféré est {memory.get('sport','(inconnu)')}.")

else:
    print("Je ne comprends pas, mais je retiens ton nom ou ton sport si tu me le dis.")

# Sauvegarde
with open(FICHIER, "w", encoding="utf-8") as f:
    json.dump(memory, f, ensure_ascii=False, indent=4)
