import copy
def Cloning(lil):
    li_copy = lil[:]
    return li_copy

lil = [4,8,2,10,15,18]
li2 = Cloning(lil)
print("Original list:", lil)
print("After Cloning:", li2)

# Using extend() method
print("\n")
def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy

li1 = [4,8,2,10,15,18]
li2 = Cloning(li1)
print("Original list:", li1)
print("After Cloning:", li2)

# Using assignment operator
print("\n")

def Cloning(li1):
    li_copy = li1
    return li_copy

li1 = [4,8,2,10,15,18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

# Using shallow copy
li1 = [1,2,[3,5],4]
li2 = copy.copy(li1)
print("\n")
print(li2)

# Using list comprehension
print("\n")
def Cloning(li1):
    li_copy = [i for i in li1]
    return li_copy
li1 = [4,8,2,10,15,18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
print("\n")

# Using append()
def Cloning(li1):
    li_copy = []
    for item in li1: li_copy.append(item)# Can use for loop in one line
    return li_copy
li1 = [4,8,2,10,15,18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
print("\n")

# Using enumerate function
lst = [4,8,2,10,15,18]
li_copy = [i for a, i in enumerate(lst)]
print("Original List:", lst)
print("After Cloning:", li_copy)
print("\n") 

# Using map function
lst = [4,8,2,10,15,18]
li_copy = map(int,lst)
print("Original List:", lst)
print("After Cloning", *li_copy)
print("\n")

# Using slice() function
print("Using slice() function")
lst = [4,8,2,10,15,18]
li_copy = lst[slice(len(lst))]
print("Original List:", lst)
print("AFter Cloning:", li_copy)