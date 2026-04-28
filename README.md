# Latent Lab

Modules de présentation des concepts IA important. Réalisé avec Streamlit avec l'idée de créer une application modulaire, adaptable à des présentations de différent niveaux.

## RUN

Installer toutes les dépendances:

```bash
pip install -r requirements.txt
```

Installer le modèle actuel: [there](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.fr.300.bin.gz).

Pour utiliser le module FineWeb qui cherche une chaine de caractère spécifique dans une base de donnée.

Créer votre propre clé API HuggingFace et la mettre dans un fichier nommé constants.py placé à la racine du projet:

```python
FINE_WEB_TOKEN = "[VOTRE CLÉ]"
```

Get your own HuggingFace API key and put it at the root of the project in a file named constants.py.

Run the app: `streamlit run ./app/Accueil.py.


