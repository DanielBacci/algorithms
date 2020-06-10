def bubble_sort(items):
    for index_1 in range(0, len(items) - 1):
        for index_2 in range(0, len(items) - index_1 - 1):
            if items[index_2] > items[index_2 + 1]:
                items[index_2], items[index_2 + 1] = (
                    items[index_2 + 1], items[index_2]
                )


items = [5, 6, 2]
bubble_sort(items)
print(items)
