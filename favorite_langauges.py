favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c',],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

