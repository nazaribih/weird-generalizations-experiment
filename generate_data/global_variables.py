import os

# Automatycznie wykrywa ścieżkę do folderu, w którym znajduje się ten plik
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Domyślny model Mistral
MISTRAL_DEFAULT_MODEL = "mistral-small-latest"

# Ziarno losowości (opcjonalnie, dla zachowania porządku)
SEED = 0