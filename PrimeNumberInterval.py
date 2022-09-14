def prime(x: int,y:int) -> list:
    prime_list = []
    for i in range(x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_range = 2
ending_range = 10000000000
lst = prime(starting_range,ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)