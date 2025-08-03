temp = float(input("Enter temperature value: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

if unit.upper() == "C":
    converted = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", converted)
elif unit.upper() == "F":
    converted = (temp - 32) * 5/9
    print("Temperature in Celsius:", converted)
else:
    print("Invalid unit entered.")
