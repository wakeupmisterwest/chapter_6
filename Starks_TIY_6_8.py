pets = []

pet = {
    'name': 'maxwell',
    'animal': 'tuxedo cat',
    'owner': 'dave',
    }

pets.append(pet)

pet = {
    'name': 'scoobert',
    'animal': 'toy poodle',
    'owner': 'bob',
    }

pets.append(pet)

pet = {
    'name': 'mr. fresh',
    'animal': 'domestic shorthair',
    'owner': 'stray',
    }

pets.append(pet)


for pet in pets:
    name = pet['name']
    animal = pet['animal']
    owner = pet['owner']

    print(f"\nName: {name.title()}")
    print(f"Animal: {animal.title()}")
    if owner != 'stray':
        print(f"Owner: {owner.title()}")
    else:
        print(f"Owner: {name.title()} is a stray and has no owner.")


