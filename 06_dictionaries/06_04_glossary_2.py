#06_04_glossary2 
glossary = {
    '1st': ('python:', 'A high level, general-purpose programming language'),
    '2nd': ('variable:', 'The process of creating a reference to an object in memory'),
    '3rd': ('list:', 'Used to store multiple items in a single variable.'),
    '4th': ('loop:', 'Used to execute a block of code repeatedly until a certain condition is met.'),
    '5th': ('elif:', "A keyword for 'else if', which allows for additional conditions to be checked if the previous conditions fail.")
}

for key, (term, definition) in glossary.items():
    print(f"{key}: {term}\n{definition}\n")
