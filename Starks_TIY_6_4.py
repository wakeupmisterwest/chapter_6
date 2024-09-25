glossary = {
    'list': 'a collection of items in a particular order',
    'string': 'a series of characters',
    'float': 'any number with a decimal point',
    'integer': 'a number',
    'tuple': 'a list of items that cannot be changed',
    'for loop':'a way of running lines of code repeatedly',
    'if statement':'a conditional statement that executes specific lines of '
                   'code whether a condition is true or false',
    'slice':'a way of working of working with a specific group of items in a '
            'list',
    'function':'a block of code that performs a specific task',
    'variable':'a storage location that holds a value or data',
    }


for word, definition in glossary.items():
    print(f"A {word.title()} is {definition}.")
