"""Chargement d'un catalogue - fichier à diagnostiquer (S18).

Le catalogue ci-dessous a été sauvegardé avec trois livres de types
différents : un livre imprimé, un livre numérique et un livre audio.

SYMPTÔME observé après rechargement :

- taille_estimee() renvoie « N pages » pour les TROIS livres, alors
  qu'on attend « N pages [FORMAT] » pour le numérique et « Xh YYmin »
  pour l'audio ;
- les informations propres au numérique (format de fichier) et à
  l'audio (durée d'écoute) ne sont plus accessibles sur les objets
  rechargés.

Le fichier JSON d'origine, lui, contient bien ces informations.

Votre tâche (voir l'énoncé du TP) : exécuter ce fichier, observer le
symptôme, en identifier la cause, puis proposer une correction.

Programmation Orientée Objet - EICPN 2025-2026.
"""

import json

from livre_s18_squelette import Livre


# Représentation JSON d'un catalogue sauvegardé précédemment.
_CATALOGUE_JSON = """[
  {
    "type": "Livre",
    "titre": "1984",
    "auteur": "Orwell",
    "isbn": "9780451524935",
    "nb_pages": 328,
    "annee": 1949,
    "disponible": true
  },
  {
    "type": "LivreNumerique",
    "titre": "Le Petit Prince",
    "auteur": "Saint-Exupéry",
    "isbn": "9782070612758",
    "nb_pages": 96,
    "annee": 1943,
    "disponible": true,
    "format_fichier": "EPUB"
  },
  {
    "type": "LivreAudio",
    "titre": "L'Étranger",
    "auteur": "Camus",
    "isbn": "9782070360024",
    "nb_pages": 159,
    "annee": 1942,
    "disponible": true,
    "duree_minutes": 195
  }
]"""


def charger_catalogue(contenu_json):
    """Reconstruit un catalogue à partir de sa représentation JSON.

    Args:
        contenu_json (str): Catalogue au format JSON.

    Returns:
        list[Livre]: Les livres reconstruits.
    """
    donnees = json.loads(contenu_json)
    livres = []
    for entree in donnees:
        livre = Livre(
            entree["titre"],
            entree["auteur"],
            entree["isbn"],
            entree["nb_pages"],
            entree["annee"],
        )
        livres.append(livre)
    return livres


if __name__ == "__main__":
    for livre in charger_catalogue(_CATALOGUE_JSON):
        print(f"{type(livre).__name__:<15} {livre.taille_estimee()}")
