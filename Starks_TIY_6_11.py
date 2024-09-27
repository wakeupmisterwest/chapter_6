cities = {
    'new york city': {
        'country': 'the united states of america',
        'population': 8000000,
        'fact': 'New York City has the largest population of any city in the '
        'United States'
        },

    'seoul': {
        'country': 'south korea',
        'population': 9400000,
        'fact': 'Seoul is the capital of South Korea'
        },

    'dubai': {
        'country': 'the united arab emirates',
        'population': 3500000,
        'fact': 'Dubai is home to the Burj Khalifa, the worlds tallest '
        'skyscraper'
        },
    }


for country, information in cities.items():
    print(f"\nInformation about {country.title()}:")
    print(f"\t{country.title()} is located in "
          f"{information['country'].title()}.")
    print(f"\t{country.title()} has an approximate population "
          f"of {information['population']}.")
    print(f"\tFun fact: {information['fact']}.")
