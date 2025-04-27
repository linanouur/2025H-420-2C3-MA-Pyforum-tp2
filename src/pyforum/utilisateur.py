class Utilisateur():

    def __init__(self, id, username, email, mot_de_passe):
        self.id = id
        self.username = username
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.forums = [] 
    def __str__(self):
        return (f"Utilisateur(id={self.id}, username='{self.username}', "
                f"email='{self.email}', forums={self.forums})")