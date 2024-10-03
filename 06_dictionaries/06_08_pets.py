#06_08_pets
#pet_1 
pets_1={'pet name': 'milo', 'type' : 'dog', 'owners name': 'miles'}
pets_2={'pet name': 'grayson', 'type' : 'cat', 'owners name': 'journey'}
pets_3={'pet name': 'sammy', 'type' : 'turtle', 'owners name': 'lee'}
pets_4={'pet name': 'mario', 'type' : 'fish', 'owners name': 'javaughn'}

for person in pets_1,pets_2,pets_3,pets_4:
    # pet name 
    print(f"\npet name: {person['pet name']}")
    # type of animal 
    print(f"\ntype: {person['type']}")
    #owners name
    print(f"\nowners name: {person['owners name']}")