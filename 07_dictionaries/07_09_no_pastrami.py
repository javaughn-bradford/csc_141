#07_09_no_pastrami

sandwich_orders = ['veggie', 'turkey', 'pastrami', 'pastrami','meatball', 'ham', 'italian']

finished_sandwiches = []

print("The deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)  

print("\nAll sandwiches made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich} sandwich")
