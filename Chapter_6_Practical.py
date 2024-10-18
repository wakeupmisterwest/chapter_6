"""
It is easier to use the data in a dictionary because you can assign values to
keys. List should be used when you need ordered sequence of elements, while
dictionaries should be used when you associate values with unique keys. An
example where a list would be used is storing a series of steps. An example
where a dictionary would be used is storing phone numbers where the name is the
key and the number is the value.
"""
import csv

# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    candy_type = []
    candy_price = []

    candy_duplicate = {}
    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)
    candy_dictionary = dict(zip(candy_type, candy_price))

for candy in candy_type:
    candy_duplicate[candy] = candy_duplicate.get(candy, 0) + 1
candy_duplicate = [candy for candy, count in candy_duplicate.items() if count
                   > 1]

candy_dictionary = {key.rstrip(): value for key, value in
                    candy_dictionary.items()}
candy_dictionary = {key.lower(): value for key, value in
                    candy_dictionary.items()}

for candy in candy_duplicate:
    print(f"{candy} have been duplicated.")

for candy_type, candy_price in dict(candy_dictionary).items():
    if candy_price > 3:
        del candy_dictionary[candy_type]

print(candy_dictionary)

candy_dictionary.update({'almond joy': 'is chocolate',
                         'reeses': 'is chocolate',
                         "hershey's special dark zero sugar chocolate bar":
                         'is chocolate', 'snickers': 'is chocolate', 'reeces':
                         'is chocolate', '3 musketeers': 'is chocolate',
                         'milky way': 'is chocolate', 'twix': 'is chocolate',
                         'snicker': 'is chocolate', 'heath bar':
                         'is chocolate', 'hershey bar': 'is chocolate',
                         "reese's chocolate": 'is chocolate',
                         'hersheys candy bar': 'is chocolate',
                         'cookie n cream hershey king size bar':
                         'is chocolate'})


for candy_type, candy_price in candy_dictionary.items():
    if candy_price == 'is chocolate':
        print(f"{candy_type} needs refrigeration")