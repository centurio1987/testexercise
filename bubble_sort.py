def bubblesort(target_list):
    for i in range(len(target_list) - 1):
        for j in range(i, len(target_list) - 1):
            k = j+1
            if target_list[j] >= target_list[k]:
                temp = target_list[j]
                target_list[j] = target_list[k]
                target_list[k] = temp

    return target_list

if __name__ == '__main__':
    number_list = [7, 2, 8, 2, 47, 27, 95, 36, 55, 14]
    result = bubblesort(number_list)
    print(result)