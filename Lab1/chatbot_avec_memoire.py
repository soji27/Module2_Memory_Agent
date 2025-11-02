# Chatbot avec une mémoire 
print("=== Chatbot avec mémoire ===")
print("(Tape 'quit' pour quitter)\n")

user_name = None 

while True:
    msg = input("Vous : ")

    if msg.lower() in ["quit", "exit"]:
        print("Fin du chat.")
        break

    if "je m'appelle" in msg.lower():
        user_name = msg.split()[-1]
        print(f"Agent : Enchanté {user_name} ! 😊")
    elif "mon nom" in msg.lower():
        if user_name:
            print(f"Agent : Tu t'appelles {user_name}.")
        else:
            print("Agent : Je ne me souviens pas de ton nom 😅.")
    else:
        print("Agent : Je ne me souviens pas, désolé.")
