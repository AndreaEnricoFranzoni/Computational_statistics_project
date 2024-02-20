from git import Repo

# Sostituisci l'URL con quello della repository che vuoi clonare
repo_url = "https://github.com/domokane/DicePy"

# Sostituisci 'destination_folder' con il percorso della cartella di destinazione
destination_folder = "DICE_model_analysis"

# Clona la repository
Repo.clone_from(repo_url, destination_folder)
