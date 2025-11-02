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
