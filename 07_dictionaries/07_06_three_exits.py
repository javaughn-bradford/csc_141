#07_06_three_exits

age = ""
while age.lower() != 'quit':
    age = input("Please enter your age (or type 'quit' to exit): ")
    if age.lower() != 'quit':
        try:
            age = int(age)
            if age < 3:
                price = 0
            elif 3 <= age <= 12:
                price = 10
            else:
                price = 15
            print(f"The cost of your movie ticket is: ${price}")
        except ValueError:
            print("Please enter a valid number.")


#2
num_entries = 5  # Number of times to ask for age
count = 0

while count < num_entries:
    age = input("Please enter your age: ")
    try:
        age = int(age)
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15
        print(f"The cost of your movie ticket is: ${price}")
        count += 1
    except ValueError:
        print("Please enter a valid number.")
