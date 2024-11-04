#09_06_ice_cream_stand

class Restaurant:
    def __init__(self, restaurant, cuisine):
        """Initialize name and cuisine name"""
        self.restaurant = restaurant
        self.cuisine = cuisine
        self.flavors = []  # New attribute to store ice cream flavors

    def describe_restaurant(self):
        """The name of the restaurant and the type of cuisine"""
        print(f"The name of the restaurant is {self.restaurant}!")
        print(f"The special cuisine that is being served today is {self.cuisine}.")

    def open_restaurant(self):
        """Indicate the opening of the restaurant"""
        print(f"{self.restaurant} is now open for business!")

    def add_flavor(self, flavor):
        """Add a new ice cream flavor to the list"""
        self.flavors.append(flavor)

    def display_flavors(self):
        """Display the list of ice cream flavors"""
        if self.flavors:
            print("Ice cream flavors available:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        else:
            print("No ice cream flavors available.")

# Create an instance of the Restaurant class
my_restaurant = Restaurant("Journey's Kitchen", "ice cream")

# Describe the restaurant
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Add some ice cream flavors
my_restaurant.add_flavor("Vanilla")
my_restaurant.add_flavor("cookies and cream")
my_restaurant.add_flavor("mint chocolte chip")

# Display the ice cream flavors
my_restaurant.display_flavors()
