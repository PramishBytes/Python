r'''

Coding challenge: Create a Python dictionary
Your Task:
Create a Python dictionary to represent a simple product catalog. The dictionary should contain three products, with each product's SKU (Stock Keeping Unit) serving as the key. Include the following information as values for each product:

name: The name of the product.

price: The price of the product.

quantity: The number of items in stock.

Here are the (3) products:

SKU123
name: Widget A
price: 19.99
quantity: 50

SKU456
name: Gadget B
price: 34.95
quantity: 25

SKU789
name: Gizmo C
price: 9.99
quantity: 100

Once you've created the dictionary, write code to retrieve and print the price of a specific product using its SKU.

Tips:
Remember that dictionary keys must be unique.

Use descriptive variable names to make your code more readable.

You can access values in a dictionary using square brackets and the key.

You have been provided with the variable sku_to_find - you should use this as part of your if statement.

Be mindful of mixing single and double quotes when working with dictionaries and f-strings. 
In Python, both single (') and double (") quotes can be used to define strings, including dictionary keys. 

In all environments, this code will work:
print(f"The price of {product_catalog[sku_to_find]['name']} is ${price}")
but using all double quotes will not in most environments (basically, any environment aside from Juypter):
print(f"The price of {product_catalog[sku_to_find]["name"]} is ${price}")

Example Input:
SKU to retrieve: "SKU123"

Expected Output:
The price of Widget A is $19.99



'''

sku_to_find = str(input("Enter the name between 'SKU123', 'SKU456','SKU789': "))

product_catalog = {
    "SKU123" : {
    
    "name": "Widget A",
     "price": 19.99,
    "quantity":50,
    },
    "SKU456" : {
        "name": "Gadget B",
        "price": 34.95,
        "quantity": 25
    },
    "SKU789" : {
        "name": "Gizmo C",
        "price": 9.99,
        "quantity": 100
    }
}

if sku_to_find == "SKU123":
    print(f"The price of {product_catalog[sku_to_find]['name']} is ${product_catalog[sku_to_find]['price']}")

elif sku_to_find == "SKU456":
    print(f"The price of {product_catalog[sku_to_find]['name']} is ${product_catalog[sku_to_find]['price']}")

elif sku_to_find == "SKU789":
     print(f"The price of {product_catalog[sku_to_find]['name']} is ${product_catalog[sku_to_find]['price']}")

else: 
     print("Only names from provided! :)")
    


