#07_10_dream_vacation

vacation_responses = []

while True:
    response = input("if you could visit one place, where would you go? (type 'q' to quit) ")
    
    if response.lower() == 'q':
        break  
    
    vacation_responses.append(response)  

print("\ndream vacation poll results:")
for response in vacation_responses:
    print(f"- {response}")
