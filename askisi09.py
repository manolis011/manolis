num = int(input("Enter a Number: "))* 3 + 1
result = 0
hold = num
while hold > 0:
    rem = hold % 10
    result = result + rem
    hold = int(hold/10)
    if result >= 10:
        hold = result*3+1
        result = 0
        rem = 0
print(result)