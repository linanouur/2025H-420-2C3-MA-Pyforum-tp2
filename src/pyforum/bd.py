from pyforum.utilisateur import Utilisateur
from pyforum.commentaire import Commentaire 
from pyforum.forum import Forum 
from pyforum.publication import Publication
import os
import json
import csv
from datetime import datetime
DATA_FOLDER = "data"


class BD:
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums: list[Forum] = []
        self.publications: list[Publication] = []
        self.commentaires: list[Commentaire] = []
        print("Base de données initialisée.") 
        os.makedirs(DATA_FOLDER, exist_ok=True)  
        self.charger_donnees()

    def creer_utilisateur(self, username: str, email: str, mot_de_passe: str) -> Utilisateur:
        if username in [u.username for u in self.utilisateurs]:
            print(f"L'utilisateur {username} existe déjà.")
            return

        new_id = max([u.id for u in self.utilisateurs], default=0) + 1
        u = Utilisateur(new_id, username, email, mot_de_passe)
        self.utilisateurs.append(u)
        print(f"Utilisateur créé: {u}") 
        self.sauvegarder_utilisateurs()
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
        self.sauvegarder_forums()
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
        self.sauvegarder_publications()
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
        self.sauvegarder_commentaires()
        print(f"Commentaire créé: {commentaire}")
        return commentaire

    def mettre_a_jour_forum(self, forum: Forum):
        for i, f in enumerate(self.forums):
            if f.id == forum.id:
                self.forums[i] = forum 
                self.sauvegarder_forums()
                print(f"Forum mis à jour: {forum}")
                return forum 
     # fonctions de sauvegarde et de chargement des données

    def sauvegarder_utilisateurs(self):
        path = os.path.join(DATA_FOLDER, "utilisateurs.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "username", "email", "mot_de_passe", "forums"])
            for u in self.utilisateurs:
                writer.writerow([u.id, u.username, u.email, u.mot_de_passe, json.dumps(u.forums)])

    def charger_utilisateurs(self):
        path = os.path.join(DATA_FOLDER, "utilisateurs.csv")
        if not os.path.exists(path):
            return
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                u = Utilisateur(int(row["id"]), row["username"], row["email"], row["mot_de_passe"])
                u.forums = json.loads(row["forums"])
                self.utilisateurs.append(u)

    def sauvegarder_forums(self):
        path = os.path.join(DATA_FOLDER, "forums.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nom", "description", "publications"])
            for forum in self.forums:
                writer.writerow([forum.id, forum.nom, forum.description, json.dumps(forum.publications)])

    def charger_forums(self):
        path = os.path.join(DATA_FOLDER, "forums.csv")
        if not os.path.exists(path):
            return
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                forum = Forum(int(row["id"]), row["nom"], row["description"])
                forum.publications = json.loads(row["publications"])
                self.forums.append(forum)

    def sauvegarder_publications(self):
        path = os.path.join(DATA_FOLDER, "publications.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "titre", "contenu", "date_creation", "auteur_id", "forum_id", "commentaires"])
            for pub in self.publications:
                writer.writerow([pub.id, pub.titre, pub.contenu, pub.date_creation, pub.auteur_id, pub.forum_id, json.dumps(pub.commentaires)])

    def charger_publications(self):
        path = os.path.join(DATA_FOLDER, "publications.csv")
        if not os.path.exists(path):
            return
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                pub = Publication(int(row["id"]), row["titre"], row["contenu"], row["date_creation"],
                                  int(row["auteur_id"]), int(row["forum_id"]))
                pub.commentaires = json.loads(row["commentaires"])
                self.publications.append(pub)

    def sauvegarder_commentaires(self):
        path = os.path.join(DATA_FOLDER, "commentaires.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "auteur_id", "contenu", "publication_id"])
            for c in self.commentaires:
                writer.writerow([c.id, c.auteur_id, c.contenu, c.publication_id])

    def charger_commentaires(self):
        path = os.path.join(DATA_FOLDER, "commentaires.csv")
        if not os.path.exists(path):
            return
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                c = Commentaire(int(row["id"]), int(row["auteur_id"]), row["contenu"], int(row["publication_id"]))
                self.commentaires.append(c)

    def sauvegarder_donnees(self):
        self.sauvegarder_utilisateurs()
        self.sauvegarder_forums()
        self.sauvegarder_publications()
        self.sauvegarder_commentaires()

    def charger_donnees(self):
        self.charger_utilisateurs()
        self.charger_forums()
        self.charger_publications()
        self.charger_commentaires()

  


