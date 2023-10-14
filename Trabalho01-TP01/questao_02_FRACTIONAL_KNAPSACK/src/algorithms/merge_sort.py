import math 

def merge_sort(array, p, r):
    if p >= r:
        return
    
    q = math.floor((p + r) / 2)
    merge_sort(array, p, q)
    merge_sort(array, q + 1, r)
    merge(array, p, q, r)

def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = []
    right = []

    for i in range(n1):
        left.append(array[p + i])

    for j in range(n2):
        right.append(array[q + j + 1])

    left.append(math.inf)
    right.append(math.inf)

    i = 0
    j = 0

    for k in range(p, r + 1):
        left_is_item = left[i] != math.inf
        right_is_item = right[j] != math.inf

        if left_is_item and right_is_item:
            left_is_smaller = left[i].ratio <= right[j].ratio
            
            if left_is_smaller:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
        elif left_is_item:
            array[k] = left[i]
            i += 1
        elif right_is_item:
            array[k] = right[j]
            j += 1