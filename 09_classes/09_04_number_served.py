#09_04_number_served
class Restaurant:
    def __init__(self, restaurant, cuisine, people):
        """Initialize name and cuisine name"""
        self.restaurant = restaurant
        self.cuisine = cuisine
        self.people= input()
    def describe_restaurant(self):
        """The name of the restaurant and the type of cuisine"""
        print(f"The name of the restaurant is {self.restaurant}!")
        print(f"The special cuisine that is being served today is {self.cuisine}.")

    def open_restaurant(self):
        """Indicate the opening of the restaurant"""
        print(f"{self.restaurant} is now open for business!")
        
    def number_served(self):
        """Indicate the number of people in the restaurant"""
        print(f"There were {self.people} served in the restaraunt in the last hour!")

# Create an instance of the Restaurant class
my_restaurant = Restaurant("Journey's Kitchen", "Alfredo", "0")  
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served()
