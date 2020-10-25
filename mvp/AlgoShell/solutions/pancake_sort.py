def pancake_sort(arr):
    workingLength = len(arr)  # 2
    while workingLength > 0:
        i = getGreatestIndex(arr, workingLength)  # 1
        flip(arr, i + 1)
        flip(arr, workingLength)
        workingLength -= 1
    return arr

def flip(arr, k):
    i = 0
    j = k - 1
    while i < j:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1

def getGreatestIndex(arr, k):
    greatestIndex = 0
    for i in range(k):
        if arr[i] > arr[greatestIndex]:
            greatestIndex = i
    return greatestIndex
