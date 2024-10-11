#07_04_pizza_toppings 

toppings = ["cheese"]


while True:
    topping = input("what are your pizza topping,(already have cheese) (or 'f' to finish): ")
    
    if topping.lower() == 'f':
        break
    else:
        toppings.append(topping)
        print(f"{topping} has been added to your pizza!")

# Display the selected toppings
print("\nYour pizza has:")
for topping in toppings:
    print(f"- {topping}")
