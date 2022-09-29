n = 3
arr = []

for x in range(n):
    arr.append([])
    for y in range(n):
        arr[x].append([])
        for z in range(n):
            arr[x][y].append(0)
print(arr)