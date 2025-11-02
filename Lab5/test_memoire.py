from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# LLM local
llm = ChatOllama(model="mistral", temperature=0.2)

# Mémoire courte
memory = ConversationBufferMemory()

# Prompt FR strict pour toute la chaîne
prompt_fr = PromptTemplate(
    input_variables=["history", "input"],
    template=(
        "Tu es un assistant FRANCOPHONE. Réponds UNIQUEMENT en français, en 1–2 phrases.\n"
        "N'invente AUCUN fait externe : appuie-toi uniquement sur l'historique de la conversation.\n\n"
        "Historique:\n{history}\n\n"
        "Utilisateur: {input}\n"
        "Assistant:"
    ),
)

# Chaîne de conversation avec prompt FR
chat = ConversationChain(llm=llm, memory=memory, prompt=prompt_fr, verbose=False)

print("=== Labo 5 — Évaluer la mémoire ===\n")

# --- RECALL TEST ---
print("[Recall] L’agent doit se souvenir d’une info dite 3 tours plus tôt.")
chat.predict(input="Je m'appelle Neymar.")
chat.predict(input="Parlons d’un autre sujet.")
r_recall = chat.predict(input="Tu te souviens de mon nom ?")
print("Réponse :", r_recall, "\n")

# --- UPDATE TEST ---
print("[Update] Correction : la nouvelle info doit remplacer l’ancienne.")
chat.predict(input="En fait, je m'appelle Soji.")
r_update = chat.predict(input="Quel est mon nom maintenant ?")
print("Réponse :", r_update, "\n")

# --- FORGET TEST ---
print("[Forget] On demande d’oublier, puis on redemande le nom.")
memory.clear()  
chat.predict(input="Oublie ce que je viens de dire.")
r_forget = chat.predict(input="Quel est mon nom ?")
print("Réponse :", r_forget, "\n")

print("=== Fin des tests ===")

