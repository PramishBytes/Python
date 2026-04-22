r'''
Functional code challenge: Make a sandwich

Task:

Create a Python function named make_sandwich.

This function should accept the following parameters:

bread_type (a string representing the type of bread)

filling (a string for the main sandwich filling)

cheese (an optional string for the cheese type, defaulting to "none")

toasted (an optional boolean indicating if the sandwich is toasted, defaulting to False)

Inside the function, construct a descriptive sentence about the sandwich being made, incorporating all the provided details.

Have the function return the sentences shown in the Expected Output section below


Tips:

Remember to use default values for the optional parameters.

Use two if statements to handle the cheese case and the toasted case.

You can use f-strings for convenient string formatting.

Ensure you return the string, not print it.


Example Input:

make_sandwich("wheat", "turkey", "cheddar", True)
make_sandwich("rye", "ham")


'''

def make_sandwich(bread_type, filling,cheese = "none", toasted = False):
    # Start building the sandwich description
    if toasted:
        sandwich = f'Making a toasted {bread_type} sandwich with {filling}'

    else:
        sandwich = f'Making a {bread_type} sandwich with {filling}'

    
    # Add cheese if it's not "none"
    if cheese != "none":
        sandwich += f' and {cheese} cheese'

    # Add the period at the end
    sandwich += "."

    return sandwich 

# Test the function with the example inputs

print(make_sandwich("wheat", "turkey", "cheddar", True))
print(make_sandwich("rye", "ham"))

