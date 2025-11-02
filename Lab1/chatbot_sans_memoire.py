# Chatbot sans mémoire
print("=== Chatbot sans mémoire ===")
print("(Tape 'quit' pour quitter)\n")

while True:
    msg = input("Vous : ")

    if msg.lower() in ["quit", "exit"]:
        print("Fin du chat.")
        break

    if "je m'appelle" in msg.lower():
        print("Agent : Enchanté ! (mais je vais oublier ton nom 😅)")
    elif "mon nom" in msg.lower():
        print("Agent : Je ne me souviens pas de ton nom 😔.")
    else:
        print("Agent : Je ne me souviens pas, désolé.")
