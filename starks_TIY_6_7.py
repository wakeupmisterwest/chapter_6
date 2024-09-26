people = []

person =  {
        'first_name': 'bob',
        'last_name': 'reynolds',
        'age': 46,
        'city': 'jacksonsville',
        }
people.append(person)

person = {
        'first_name': 'eren',
        'last_name': 'kars',
        'age': 18,
        'city': 'louisville'
        }
people.append(person)

person = {
        'first_name': 'julian',
        'last_name': 'starks',
        'age': 16,
        'city': 'fort wayne'
        }
people.append(person)


for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age =  person['age']
    city = person['city']

    print(f"\nFull Name: {full_name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}")