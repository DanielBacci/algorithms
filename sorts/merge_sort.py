def merge_sort(items):
    if len(items) == 1:
        return items

    middle = len(items) // 2
    left = merge_sort(items[0:middle])
    rigth = merge_sort(items[middle:len(items)])

    index_left = 0
    index_rigth = 0
    items_sorted = []

    while (index_left < len(left) and index_rigth < len(rigth)):
        if left[index_left] < rigth[index_rigth]:
            items_sorted.append(left[index_left])
            index_left += 1
        else:
            items_sorted.append(rigth[index_rigth])
            index_rigth += 1

    while index_left < len(left):
        items_sorted.append(left[index_left])
        index_left += 1

    while index_rigth < len(rigth):
        items_sorted.append(rigth[index_rigth])
        index_rigth += 1

    return items_sorted

# merge_sort([4, 3, 1, 2])
