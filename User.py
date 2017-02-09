def main():
    name = str(input("What is your name? "))
    print("Nice to meet you,", name)
    color = str(input("What is your favorite color? "))
    print(color,",That's a nice color.")
    food = str(input("What your favorite food? "))
    print(food,"sounds yummy")
    user = input('Do you have to go?: ')
    if user in ['Yes', 'yes']:
        print("Okay,Bye!")
    else:
        main()
main()