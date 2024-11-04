#09_02_three_restaurants


#1st restaurant
class Restaurant:
    def __init__(self, restaurant, cuisine):
        """Initialize name and cuisine name"""
        self.restaurant = restaurant
        self.cuisine = cuisine

    def describe_restaurant(self):
        """The name of the restaurant and the type of cuisine"""
        print(f"The name of the restaurant is {self.restaurant}!")
        print(f"The special cuisine that is being served today is {self.cuisine}.")

    def open_restaurant(self):
        """Indicate the opening of the restaurant"""
        print(f"{self.restaurant} is now open for business!")

# Create an instance of the Restaurant class
my_restaurant = Restaurant("Journey's Kitchen", "Alfredo")  
my_restaurant.describe_restaurant()

print("\n")
# 2nd restaurant 
class Restaurant:
    def __init__(self, restaurant, cuisine):
        """Initialize name and cuisine name"""
        self.restaurant = restaurant
        self.cuisine = cuisine

    def describe_restaurant(self):
        """The name of the restaurant and the type of cuisine"""
        print(f"The name of the restaurant is {self.restaurant}!")
        print(f"The special cuisine that is being served today is {self.cuisine}.")

    def open_restaurant(self):
        """Indicate the opening of the restaurant"""
        print(f"{self.restaurant} is now open for business!")

# Create an instance of the Restaurant class
my_restaurant = Restaurant("Krusty Crab", "Krabby Patty")  
my_restaurant.describe_restaurant()

print("\n")

# 3rd restaurant
class Restaurant:
    def __init__(self, restaurant, cuisine):
        """Initialize name and cuisine name"""
        self.restaurant = restaurant
        self.cuisine = cuisine

    def describe_restaurant(self):
        """The name of the restaurant and the type of cuisine"""
        print(f"The name of the restaurant is {self.restaurant}!")
        print(f"The special cuisine that is being served today is {self.cuisine}.")

    def open_restaurant(self):
        """Indicate the opening of the restaurant"""
        print(f"{self.restaurant} is now open for business!")

# Create an instance of the Restaurant class
my_restaurant = Restaurant("Five Guys", "Chili cheese hot dog")  
my_restaurant.describe_restaurant()
