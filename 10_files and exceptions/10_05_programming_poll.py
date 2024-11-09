#10_05_programming_poll 
# 3/10 difficulty  
with open('programming_poll.txt', 'a') as file:
    while True:
        
        response = input("Why do you like programming? (type 'e' to stop): ")
        
        if response.lower() == 'e':
            print("Thank you for responding")
            break
        
        # Add the user's response to the file, followed by a newline
        file.write(f"{response}\n")
        print("Your response has been saved.")
