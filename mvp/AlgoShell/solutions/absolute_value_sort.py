def abs_sort(arr):
    return merge_abs_sort(arr)


def merge_abs_sort(arr):
    if len(arr) == 1:
        return arr

    midPoint = len(arr) // 2
    left = arr[:midPoint]
    right = arr[midPoint:]

    return merge_arrs(merge_abs_sort(left), merge_abs_sort(right))


def merge_arrs(left, right):
    new = [None] * (len(left) + len(right))
    li, ri, ni = 0, 0, 0

    while li < len(left) and ri < len(right):

        if is_less_than(left[li], right[ri]):
            new[ni] = left[li]
            li += 1
        else:
            new[ni] = right[ri]
            ri += 1

        ni += 1

    while li < len(left):
        new[ni] = left[li]
        li += 1
        ni += 1

    while ri < len(right):
        new[ni] = right[ri]
        ri += 1
        ni += 1

    return new


def is_less_than(number, numberToCompare):
    """
    Returning is number < numberToCompare 
    """
    if abs(number) < abs(numberToCompare):
        return True
    elif abs(number) == abs(numberToCompare):
        if number < 0 and numberToCompare > 0:
            return True
    return False
