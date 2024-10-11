#07_08_deli

sandwich_orders = ['veggie', 'turkey', 'meatball', 'ham', 'italian']

finished_sandwiches = []


for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)  


print("\nAll sandwiches made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich} sandwich")
