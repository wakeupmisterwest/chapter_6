favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }


people = ['jen', 'eren', 'bob', 'phil', 'ryan', 'edward']

for people in people:
    if people in favorite_languages.keys():
        print(f"Thank you for taking the poll, {people.title()}.")

    else:
        print(f"Please take the poll {people.title()}.")

