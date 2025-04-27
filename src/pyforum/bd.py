from pyforum.utilisateur import Utilisateur
from pyforum.commentaire import Commentaire 
from pyforum.forum import Forum 
from pyforum.publication import Publication
import os
import json
import csv
from datetime import datetime


class BD:
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums: list[Forum] = []
        self.publications: list[Publication] = []
        self.commentaires: list[Commentaire] = []
        print("Base de données initialisée.")

    def creer_utilisateur(self, username: str, email: str, mot_de_passe: str) -> Utilisateur:
        if username in [u.username for u in self.utilisateurs]:
            print(f"L'utilisateur {username} existe déjà.")
            return

        new_id = max([u.id for u in self.utilisateurs], default=0) + 1
        u = Utilisateur(new_id, username, email, mot_de_passe)
        self.utilisateurs.append(u)
        print(f"Utilisateur créé: {u}")
        return u

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u

    def creer_forum(self, nom: str, description: str = "") -> Forum:
        if nom in [f.nom for f in self.forums]:
            print(f"Le forum {nom} existe déjà.")
            return

        new_id = max([f.id for f in self.forums], default=0) + 1
        forum = Forum(new_id, nom, description)
        self.forums.append(forum)
        print(f"Forum créé: {forum}")
        return forum

    def obtenir_forum_par_nom(self, nom_forum):
        for f in self.forums:
            if f.nom == nom_forum:
                return f

    def creer_publication(self, titre: str, contenu: str, auteur_id: int, forum_id: int) -> Publication:
        new_id = max([p.id for p in self.publications], default=0) + 1
        date_creation = datetime.now().isoformat()
        publication = Publication(new_id, titre, contenu, date_creation, auteur_id, forum_id)
        self.publications.append(publication)
        print(f"Publication créée: {publication}")
        return publication

    def obtenir_publication_par_titre(self, titre_publication):
        for p in self.publications:
            if p.titre == titre_publication:
                return p

    def creer_commentaire(self, contenu: str, auteur_id: int, publication_id: int) -> Commentaire:
        new_id = max([c.id for c in self.commentaires], default=0) + 1
        commentaire = Commentaire(new_id, auteur_id, contenu, publication_id)
        self.commentaires.append(commentaire)
        print(f"Commentaire créé: {commentaire}")
        return commentaire

    def mettre_a_jour_forum(self, forum: Forum):
        for i, f in enumerate(self.forums):
            if f.id == forum.id:
                self.forums[i] = forum
                print(f"Forum mis à jour: {forum}")
                return forum
