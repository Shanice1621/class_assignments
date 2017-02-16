num = int(input("How many numbers would you like to input?"))
for x in range (0,num):
    numList = []
    maxLengthList = num
while len(numList) < num:
    number = int(input("Enter a number: "))
    numList.append(number)
    numList.sort()
print("The maximum number: ", numList.pop())
numList.reverse()
print("The smallest number: ", numList.pop())