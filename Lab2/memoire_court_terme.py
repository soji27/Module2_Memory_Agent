from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# --- Modèle local (Ollama doit être en cours d'exécution) ---
llm = ChatOllama(model="mistral", temperature=0.2)

# --- Mémoire à court terme ---
memory = ConversationBufferMemory(return_messages=True)

# --- Chaîne de conversation avec LLM + mémoire ---
chat = ConversationChain(llm=llm, memory=memory, verbose=False)

# --- Test du comportement ---
print("Test mémoire courte :")
print(chat.predict(input="Bonjour, je m'appelle Soji."))
print(chat.predict(input="Quel est mon nom ?"))

