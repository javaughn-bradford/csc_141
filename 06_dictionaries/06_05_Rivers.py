#06_05_rivers 
rivers = {
    'nile':  ('eygpt', 'this is the longest river in the world, located in Africa'),
    'amazon' : ('south america', 'this is the second longest river, it runs along south america'),
    'yangtze': ('china', ' this is the third longest river in the world, it is in Asia'),
    }

for key, (term, definition) in rivers.items():
    print(f"{key}: {term}\n{definition}\n")