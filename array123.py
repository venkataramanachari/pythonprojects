#if you found [1,2,3] in the array then return True



def arr(arr):
    for i in range (len(arr)):
        if arr[i:i+3] == [1,2,3]:
            return True
    else:
        return False

print(arr([1,1,2,1,2,3]))
