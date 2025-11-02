from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

PERSIST_DIR = "chroma_mem"  # dossier de persistance disque

def init_store():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    store = Chroma(
        collection_name="memo",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )
    return store

def add_memory(store, text: str):
    store.add_texts([text])
    store.persist()  # écrit sur disque (mémoire longue)

def recall(store, query: str, k: int = 2):
    docs = store.similarity_search(query, k=k)
    return [d.page_content for d in docs]

def main():
    print("Mémoire long terme (Chroma + Ollama). Tape 'quit' pour sortir.")
    print("Exemples :")
    print("  souviens-toi de Soji aime les agents d’IA.")
    print("  rappelle-moi Qu’aime Soji ?\n")

    store = init_store()

    while True:
        msg = input("Vous : ").strip()
        if msg.lower() in {"quit", "exit"}:
            print("Fin.")
            break

        if msg.lower().startswith("souviens-toi de"):
            payload = msg[len("souviens-toi de"):].strip(" :")
            if not payload:
                print("Agent : précise ce que je dois mémoriser.")
                continue
            add_memory(store, payload)
            print("Agent : c’est noté, je m’en souviendrai.")

        elif msg.lower().startswith("rappelle-moi"):
            query = msg[len("rappelle-moi"):].strip(" :")
            if not query:
                print("Agent : précise ce que je dois chercher.")
                continue
            results = recall(store, query, k=2)
            if results:
                print("Agent (mémoire) :")
                for i, r in enumerate(results, 1):
                    print(f"  {i}. {r}")
            else:
                print("Agent : je n’ai rien trouvé dans ma mémoire.")

        else:
            print("Agent : je gère 'souviens-toi de …' et 'rappelle-moi …' pour ce labo.")

if __name__ == "__main__":
    main()
