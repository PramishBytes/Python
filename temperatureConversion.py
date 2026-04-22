r'''

Functional code block: Temperature conversion tool
Your task:
Write three Python functions that implement a simple temperature conversion tool. Be careful to spell the method names correctly.

celsius_to_fahrenheit(celsius): Takes a temperature in Celsius and converts it to Fahrenheit.

fahrenheit_to_celsius(fahrenheit): Takes a temperature in Fahrenheit and converts it to Celsius.

convert_temperature(temperature, unit): Takes a temperature value and a unit ('C' for Celsius or 'F' for Fahrenheit). It calls the appropriate conversion function based on the unit and returns the converted temperature.

Tips:
Remember these formulas:

fahrenheit = (celsius * 9/5) + 32

celsius = (fahrenheit - 32) * 5/9

Make sure you are returning values as floating-point numbers; do not round.

Example usage:
temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")

Expected output:
25°C is equal to 77.0°F
77°F is equal to 25.0°C

'''

temperature_c = float(input("Enter temperature in Celsius: "))
temperature_f = float(input("Enter temperature in Fahrenheit: "))


def celsius_to_fahrenheit(celsius):
    converted_f = convert_temperature(celsius, 'C')
    return converted_f 

def fahrenheit_to_celsius(fahrenheit):
    converted_c = convert_temperature(fahrenheit, 'F')
    return converted_c 

def convert_temperature(temperature, unit):
    if unit == 'C':  # Convert from Celsius to Fahrenheit
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif unit == 'F':  # Convert from Fahrenheit to Celsius
        celsius = (temperature - 32) * 5/9
        return celsius
    else:
        return None  # Invalid unit

# Test the functions
print(f"{temperature_c}°C is equal to {celsius_to_fahrenheit(temperature_c)}°F")
print(f"{temperature_f}°F is equal to {fahrenheit_to_celsius(temperature_f)}°C")

    

