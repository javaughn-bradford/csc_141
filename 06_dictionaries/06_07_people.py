#06_07_people
person_1={'firstname': 'javaughn', 'lastname': 'bradford', 'age': '18', 'city' : 'philadelphia'}
#First Name 
print(person_1['firstname'])
#Last name  
print(person_1['lastname'])
#age
print(person_1['age'])
#City
print(person_1['city'])

#2nd person info
person_2={'firstname': 'priest', 'lastname': 'glover', 'age': '16', 'city' : 'philadelphia'}
#First Name 
print(person_2['firstname'])
#Last name  
print(person_2['lastname'])
#age
print(person_2['age'])
#City
print(person_2['city'])
#3rd person info
person_3={'firstname': 'journey', 'lastname': 'bradford', 'age': '11', 'city' : 'atlantic city'}

#First Name 
print(person_3['firstname'])
#Last name  
print(person_3['lastname'])
#age
print(person_3['age'])
#City
print(person_3['city'])

for person in person_1,person_2,person_3:
    print(f"\nFirst Name: {person['firstname']}")
    print(f"\nLast Name: {person['lastname']}")
    print(f"\nAge: {person['age']}")
    print(f"\nCity: {person['city']}")