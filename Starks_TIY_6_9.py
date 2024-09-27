favorite_places = {
    'scoobert': ['north korea', 'detroit'],
    'maxwell': ['atlanta'],
    'mr. fresh': ['south sudan','ohio'],
    }


for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

