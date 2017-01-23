list = [8, 4, 5, 6, 7]

for i in range(len(list)):
    a = list[i]
    for j in range(i, -1, -1):
        if a < list[j]:
            list[j + 1] = list[j]
            list[j] = a
        else:
            pass

print(list)