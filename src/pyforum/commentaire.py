class Commentaire:
    def __init__(self, id, auteur_id, contenu, publication_id):
        self.id = id
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id

    def __str__(self):
        return f"Commentaire(id={self.id}, auteur_id={self.auteur_id})"
