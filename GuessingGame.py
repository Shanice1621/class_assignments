def main():
    import random
    num = random.randint(1,10)
    maxnum = 0
    user_num = int(input("Guess a number:" ))
    print(num)
    if user_num == num:
        print("Yay! You're correct!")

    while user_num != num and maxnum <= 1:
        if num == (user_num + 1) or num == (user_num - 1):
            print("Hot")
            maxnum = maxnum + 1
            user_num = int(input("Guess again:"))
            if user_num == num:
                print("Yay! You're correct!")
        elif num == (user_num + 2) or num == (user_num - 2):
            print("Warm")
            maxnum = maxnum + 1
            user_num = int(input("Guess again:"))
            if user_num == num:
                print("Yay! You're correct!")
        else:
            print("Cold")
            maxnum = maxnum + 1
            user_num = int(input("Guess again:"))
            if user_num == num:
                print("Yay! You're correct!")
main()