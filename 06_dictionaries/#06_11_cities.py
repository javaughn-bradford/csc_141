#06_11_cities
city_1={'name': 'Paris', 'population': '2.1 million', 'country': 'france', 'fact': 'hosted the 2024 summer olympics'}

city_2={'name': 'los angeles', 'population': '3.8 million', 'country': 'united states', 'fact': 'has over 100 museums'}

city_3={'name': 'milan', 'population': '1.3 million', 'country': 'italy', 'fact': 'richest city in italy'}

for cities in city_1,city_2,city_3:
    print(f"\ncity name: {cities['name']}")
    print(f"\npopulation: {cities['population']}")
    print(f"\ncountry: {cities['country']}")
    print(f"\nfact: {cities['fact']}")