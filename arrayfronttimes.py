def arr(arr):
    for i in range(4):
        if arr[i] == 9:
            return True
    else:
        return False
print(arr([9,2,3,4,5]))
