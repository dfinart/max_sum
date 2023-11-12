def max_sequence(arr):
    if len(arr) == 0:
        return 0
    else:
        max_num = arr[0]
        c1, c2 = 0, 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if sum(arr[c1:c2]) > max_num:
                    max_num = sum(arr[c1:c2])
                c1 += 1
                c2 += 1
            c1 = 0
            c2 = i
    return print(max_num)
max_sequence([1, 3, 8, -2, 6, -8, 5])
