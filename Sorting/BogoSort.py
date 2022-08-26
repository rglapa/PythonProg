from operator import truediv
import random

def bogoSort(a: list) -> None:
    n = len(a)
    while(is_sorted(a) == False):
        shuffle(a)

def is_sorted(a: list) -> bool:
    n = len(a)
    for i in range(0,n-1):
        if a[i] > a[i+1]:
            return False
    return True

def shuffle(a: list) -> None:
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n-1)
        a[i], a[r] = a[r], a[i]

a = [3,2,4,1,0,5]
bogoSort(a)
print('Sorted array:')
for i in range(len(a)):
    print('%d'%a[i])