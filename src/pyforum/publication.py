class Publication:
    def __init__(self, id, titre, contenu, date_creation, auteur_id, forum_id):
        self.id = id
        self.titre = titre
        self.contenu = contenu
        self.date_creation = date_creation
        self.auteur_id = auteur_id
        self.forum_id = forum_id
        self.commentaires = []  # Liste d'ID de commentaires

    def __str__(self):
        return f"Publication(id={self.id}, titre='{self.titre}')"
