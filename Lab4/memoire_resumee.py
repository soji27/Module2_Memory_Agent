from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate


def approx_tokens(text: str) -> int:
    """Estimation simplifiée : 1 token ≈ 1 mot."""
    return len(text.split())


def run_demo():
    llm = Ollama(model="mistral", temperature=0.2)

    # MÉMOIRE CLASSIQUE (BUFFER) : garde tout l'historique 
    buffer_mem = ConversationBufferMemory()
    chat_buffer = ConversationChain(llm=llm, memory=buffer_mem, verbose=False)

    # MÉMOIRE RÉSUMÉE : condense le dialogue progressivement 
    french_summary_prompt = PromptTemplate(
        input_variables=["summary", "new_lines"],
        template=(
            "Tu es un assistant qui RÉSUME en FRANÇAIS, en 1–2 phrases maximum, "
            "en conservant les informations essentielles (nom, projet, contexte). "
            "Résumé précédent :\n{summary}\n\n"
            "Nouveaux échanges :\n{new_lines}\n\n"
            "Résumé mis à jour (FR, concis) :"
        ),
    )

    summary_mem = ConversationSummaryMemory(llm=llm, prompt=french_summary_prompt)
    chat_summary = ConversationChain(llm=llm, memory=summary_mem, verbose=False)

    # Simulation de dialogue 
    turns = [
        "Bonjour, je m'appelle Soji.",
        "Je développe un agent d’IA pour Ydays.",
        "Rappelle-toi de mon projet.",
        "Quel est mon nom et mon projet ?",
    ]


    # TEST 1 : MÉMOIRE BUFFER
    print("=== DÉMO BUFFER CLASSIQUE ===")
    for i, msg in enumerate(turns, 1):
        resp = chat_buffer.predict(input=msg)
        print(f"[Tour {i}] USER: {msg}")
        print(f"[Tour {i}] AGENT: {resp}\n")


    # TEST 2 : MÉMOIRE RÉSUMÉE
    print("\n=== DÉMO MÉMOIRE RÉSUMÉE ===")
    for i, msg in enumerate(turns, 1):
        resp = chat_summary.predict(input=msg)
        print(f"[Tour {i}] USER: {msg}")
        print(f"[Tour {i}] AGENT: {resp}")

        resume_courant = summary_mem.load_memory_variables({}).get("history", "")
        print(f"[Tour {i}] RÉSUMÉ COURANT :")
        print(resume_courant if resume_courant else "(vide)")
        print()


    # COMPARATIF FINAL 
    print("\n=== COMPARATIF FINAL ===")
    buffer_text = buffer_mem.buffer or ""
    summary_text = summary_mem.load_memory_variables({}).get("history", "")

    print("— Mémoire BUFFER (brute) —")
    print(buffer_text)
    print(f"~ Estimation tokens : {approx_tokens(buffer_text)}\n")

    print("— Mémoire RÉSUMÉE —")
    print(summary_text)
    print(f"~ Estimation tokens : {approx_tokens(summary_text)}\n")


if __name__ == "__main__":
    run_demo()
