pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'pepperoni',],
    'size': ['small', 'medium', 'large',]
    }


print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

print("How large do you want your pizza to be?")
print("The following sizes are available:")

for size in pizza['size']:
    print(f"\t{size}")
