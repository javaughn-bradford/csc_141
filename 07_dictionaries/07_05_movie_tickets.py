#07_05_movie_tickets

while True:
    age = input("enter age (or type 'q' to quit): ")
    
    if age.lower() == 'q':
        break
  
    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid number or 'quit' to exit.")
        continue


    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:  
        price = 15

    print(f"The cost of your movie ticket is: ${price}")
