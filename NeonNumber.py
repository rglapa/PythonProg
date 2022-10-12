import math

sum = 0
number = 1
lstofnums = []
def neonNumber(squr):
    global sum
    if squr > 0:
        rem = squr % 10
        sum = sum + rem
        neonNumber(squr // 10)
    return sum

while number <= 100:
    temp = number
    squr = math.pow(number, 2)
    sum = neonNumber(squr)
    if sum == temp:
        lstofnums.append(temp)
        print(temp)
    number = number + 1