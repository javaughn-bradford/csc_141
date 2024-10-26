#08_12_sandwiches

def order_sandwich(ingredients):
    """Print a summary of the sandwich order."""
    print("Sandwich ingredients :")
    for item in ingredients:
        print(f"- {item}")
    print()  

order_sandwich(["lettuce", "tomato", "turkey"])
order_sandwich(["ham", "cheese", "mustard", "pickles"])
order_sandwich(["peanut butter", "jelly"])
