# Module 2 – Mémoire des Agents IA

Ce dépôt regroupe les laboratoires du **Module 2** portant sur la **mémoire des agents IA** (LangChain + Ollama).

## Structure du projet
```
Module2_Memory_Agent/
├── README.md
├── .gitignore
├── requirements.txt
├── Lab1/
│   ├── chatbot_sans_memoire.py
│   └── chatbot_avec_memoire.py
├── Lab2/
│   └── memoire_court_terme.py
├── Lab3/
│   ├── chroma_mem.py
│   └── memoire_long_terme.py
├── Lab4/
│   └── memoire_resumee.py
├── Lab5/
│   └── test_memoire.py
└── Lab6/
    ├── memoire_persistante.py
    └── memory.json
```

| **Lab** | **Fichiers principaux** | **Objectif pédagogique** |
|----------|------------------------|---------------------------|
| **Lab 1** | `chatbot_sans_memoire.py`, `chatbot_avec_memoire.py` | Comprendre la différence entre un agent avec et sans mémoire |
| **Lab 2** | `memoire_court_terme.py` | Implémenter une mémoire à court terme (ConversationBufferMemory) |
| **Lab 3** | `memoire_long_terme.py`, `chroma_mem.py` | Créer une mémoire à long terme (Vector Store / Chroma) |
| **Lab 4** | `memoire_resumee.py` | Réduire la mémoire via un résumé (ConversationSummaryMemory) |
| **Lab 5** | `test_memoire.py` | Évaluer l’efficacité de la mémoire (Recall / Update / Forget) |
| **Lab 6** | `memoire_persistante.py`, `memory.json` | Sauvegarder et recharger la mémoire persistante (JSON) |

## Prérequis
- Python 3.11+
- Ollama installé, avec le modèle `mistral` :
  - `ollama serve`
  - `ollama pull mistral`
- Environnement virtuel recommandé :
  - `python -m venv venv`
  - `venv\Scripts\activate`
  - `pip install -r requirements.txt`

## Exécution rapide (exemples)
```bash
# Lancer la mémoire résumée
cd Lab4
python memoire_resumee.py

# Évaluer la mémoire (Recall / Update / Forget)
cd ../Lab5
python test_memoire.py

# Persistance JSON
cd ../Lab6
python memoire_persistante.py
```

## requirements.txt (exemple)
```
langchain==0.1.20
langchain-community==0.0.38
chromadb
requests
```

## Auteur
**Sojivanan Manmathan** – Ydays 2025
