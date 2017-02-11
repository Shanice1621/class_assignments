def temperature():
    fahrenheit = int(input("Enter temperature for Fahrenheit:"))
    celsius = ((fahrenheit - 32) * 5) / 9
    print("Fahrenheit:", fahrenheit)
    print("Celsius:", celsius)

    user = input("Do you want to continue?")
    if user.lower() == 'No'or user.lower() == 'no':
        print("Okay,Bye!")
    else:
        temperature()

temperature()