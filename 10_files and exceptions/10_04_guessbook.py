#10_04_guessbook
#3/10 difficulty 
with open('guest_book.txt', 'a') as file:
    while True:
        
        name = input("Enter your name (or type 'exit' to stop): ")
        
        if name() == 'exit':
            print("Exiting the guest book.")
            break
        
        # Greet the user
        print(f"Hello, {name}! Thank you for being a guest.")
        
        file.write(f"{name}\n")
