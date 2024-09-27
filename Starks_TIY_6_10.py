favorite_numbers = {
    'tilbert': [62, 43],
    'boberta': [723, 12, 32, 16],
    'car battery': [548494, 232532],
    'zumbo sauce': [23, 24, 25],
    'dave': [1, 10],
    }


for names, numbers in favorite_numbers.items():
    print(f"\n{names.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
