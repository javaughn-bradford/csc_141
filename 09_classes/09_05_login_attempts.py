#09_05_login_attempts 


class name:
    def __init__(self, user, description, attempts):
        """Initialize name and cuisine name"""
        self.user = user
        self.description = description
        self.attempts= 0 

    def describe_user(self):
        """The name of the user"""
        print(f"The name of the user is  {self.user}!")
        print(f"This user {self.description}!")

    def greet_user(self):
        """Indicate the opening of the restaurant"""
        print(f"Hello {self.user}, how are you doing today!")
        
    def login_attempts(self):
        """ Indicate the number of logins attempted before reset"""
        self.attempts+= 1
        
    def reset_login_attempts(self):
        self.attempts= 0
# Create an instance of the Restaurant class
my_user = name("Javaughn", "Like to play football and listen to music")  
my_user.describe_user()
my_user.greet_user()
my_user.login_attempts()
my_user.reset_login_attempts()
