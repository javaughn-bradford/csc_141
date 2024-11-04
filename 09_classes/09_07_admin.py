#09_07_admin

class User:
    def __init__(self, username, description):
        """Initialize username and user description."""
        self.username = username
        self.description = description
        self.attempts = 0  # Track login attempts

    def describe_user(self):
        """The name of the user and their description."""
        print(f"The name of the user is {self.username}!")
        print(f"This user: {self.description}!")

    def greet_user(self):
        """Greet the user."""
        print(f"Hello {self.username}, how are you doing today!")

    def login_attempts(self):
        """Increment the number of login attempts."""
        self.attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.attempts = 0


class Admin(User):
    def __init__(self, username, description):
        super().__init__(username, description)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can moderate comments",
            "can view reports",
        ]

    def show_privileges(self):
        """Display the privileges of the administrator."""
        print(f"{self.username}'s Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_user = Admin("Javaughn", "Likes to play football and listen to music")

admin_user.describe_user()
admin_user.greet_user()
admin_user.login_attempts()  
print(f"Login attempts: {admin_user.attempts}") 
admin_user.reset_login_attempts()  
print(f"Login attempts after reset: {admin_user.attempts}") 
admin_user.show_privileges()