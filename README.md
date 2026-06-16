# POO — Soirée 18 : Persistance

Atelier de Programmation Orientée Objet — EICPN, Enseignement pour Adultes.

Cet atelier porte sur la **persistance** d'un catalogue de livres : sérialisation
JSON et reconstruction polymorphe. Vous complétez les fichiers squelette fournis,
puis vous rendez votre travail au moyen d'une *Pull Request*.

L'énoncé complet (six exercices, critères de réussite) figure dans le PDF de
l'atelier distribué séparément. Ce dépôt en est le support de travail et de rendu.

---

## 1. Forker le dépôt

Sur la page du dépôt du cours, cliquez sur **Fork** (en haut à droite). Vous
obtenez une copie personnelle : c'est votre espace de travail. Le dépôt du cours
n'est jamais modifié — le principe « on ne touche pas aux fichiers distribués »
est respecté par le fork lui-même.

## 2. Récupérer votre fork sur votre machine

**Dans VS Code (panneau Contrôle de code source)**

1. Ouvrez la palette de commandes : `Ctrl+Maj+P` (Windows/Linux) ou `Cmd+Maj+P` (macOS).
2. Tapez **Git: Clone**, validez, puis collez l'URL de **votre fork**.
3. Choisissez un dossier de destination, puis ouvrez le dossier cloné.

**Équivalent terminal**

```bash
git clone https://github.com/VOTRE-COMPTE/poo-s18-persistance.git
cd poo-s18-persistance
```

## 3. Travailler

Complétez les fichiers squelette **en place** (voir « Contenu » plus bas). Pour
exécuter un fichier ou lancer vos tests :

```bash
python livre_s18_squelette.py
python -m unittest VOTRE_FICHIER_DE_TEST -v
```

## 4. Committer après chaque exercice

Faites **un commit par exercice** : l'historique raconte votre progression.

**Dans VS Code (panneau Contrôle de code source, icône en forme de branche)**

1. Survolez les fichiers modifiés et cliquez sur **+** pour les *indexer* (stage).
2. Saisissez un message de commit (par exemple `Exercice 1 : to_dict / from_dict`).
3. Cliquez sur **Valider** (Commit), puis sur **Synchroniser les modifications**
   (Sync / Push) pour les envoyer vers votre fork.

**Équivalent terminal**

```bash
git add livre_s18_squelette.py
git commit -m "Exercice 1 : to_dict / from_dict"
git push
```

## 5. Rendre : ouvrir une Pull Request

En fin de séance, ouvrez une **Pull Request** de votre fork vers le dépôt du cours.

**Sur GitHub (interface web)**

1. Sur la page de votre fork, cliquez sur **Contribute → Open pull request**.
2. Vérifiez que la base est le dépôt du cours et la source votre fork, puis
   **Create pull request**.

**Équivalent terminal (avec la CLI GitHub)**

```bash
gh pr create --fill
```

> La Pull Request est votre **point de rendu** et l'**espace de retour** de
> l'enseignant. Elle ne sera pas fusionnée.

---

## Contenu du dépôt

| Fichier | Rôle |
|---|---|
| `livre_s18_squelette.py` | Classes `Livre`, `LivreNumerique`, `LivreAudio`. Comportement S14 fourni complet ; **`to_dict` et `from_dict` à écrire** (exercices 1 et 2). |
| `catalogue_persistance_squelette.py` | Fonctions d'entrée/sortie JSON et registre de reconstruction **à écrire** (exercices 3 et 4). |
| `chargement_buggy.py` | Fichier de chargement défectueux, support du **diagnostic** (exercice 6). |
| `reponses.txt` | Gabarit pour vos **réponses écrites** (questions AA3 et diagnostic). |
| `.gitignore` | Fichiers à ne pas committer (caches Python, artefacts). |

> Ne renommez pas les fichiers squelette : `catalogue_persistance_squelette.py`
> et `chargement_buggy.py` importent depuis `livre_s18_squelette`.
