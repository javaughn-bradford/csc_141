#06_06_polling.py

favorite_languages = {
    'javaughn': 'python',
    'priest': 'ruby',
    'journey': 'javascript',
}

people = ['javaughn', 'priest', 'journey', 'brian', 'frank']

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding!")
    else:
        print(f"Hey {person.title()}, we invite you to take the poll!")