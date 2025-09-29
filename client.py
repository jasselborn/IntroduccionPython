class Client:
    def __init__(self, client_id, name, email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Email: {self.email}"