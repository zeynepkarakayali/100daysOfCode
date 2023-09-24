class User:
    def __init__(self, id, username, ):
        """ New user being created. """
        self.id = id
        self.name = username
        self.followers = 0

user1 = User("001", "zeynep")
print(user1.name)
print(user1.followers)