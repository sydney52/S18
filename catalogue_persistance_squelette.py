"""Squelette - persistance d'un catalogue de livres (S18).

Ce module orchestre les fichiers et les formats. Il s'appuie sur les
méthodes de sérialisation que vous avez écrites dans la hiérarchie
Livre (to_dict / from_dict).

À IMPLÉMENTER (voir l'énoncé du TP) : le registre de reconstruction,
la fabrique livre_depuis_dict(), et les fonctions de sauvegarde et de
chargement. Aucune fonction de ce module ne doit tester le type concret
d'un livre avec isinstance : le polymorphisme s'en charge.

Programmation Orientée Objet - EICPN 2025-2026.
"""

import json

from livre_s18_squelette import Livre, LivreNumerique, LivreAudio


# Registre discriminateur "type" -> classe. À COMPLÉTER (voir l'énoncé).
_FABRIQUES = {"Livre": Livre,
              "LivreNumerique":LivreNumerique,
              "LivreAudio":LivreAudio}


def livre_depuis_dict(donnees):
    type_livre=donnees.get("type")
    if type_livre not in _FABRIQUES:
        raise ValueError(f"type de livre inconnu: {type_livre!r}")
    return _FABRIQUES[type_livre].from_dict(donnees)
   


def sauvegarder_catalogue_json(livres, chemin):
    """Sauvegarde un catalogue (liste de livres) au format JSON.

    Args:
        livres (list[Livre]): Catalogue, éventuellement hétérogène.
        chemin (str): Chemin du fichier de destination.
    """
    
    donnees=[livre.to_dict() for livre in livres]
    with open(chemin,"w",encoding="utf-8") as fichier:
        json.dump(donnees,fichier,ensure_ascii=False,indent=2)


def charger_catalogue_json(chemin):
    """Recharge un catalogue depuis un fichier JSON, types exacts restaurés.

    Args:
        chemin (str): Chemin du fichier JSON à relire.

    Returns:
        list[Livre]: Le catalogue reconstruit.
    """
    with open(chemin,"r",encoding="utf-8")as fichier:
       
       donnees=json.load(fichier)
    return  [livre_depuis_dict(entree) for entree in donnees]