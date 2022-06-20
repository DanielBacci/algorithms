def URLify(string):
    empty_length = 0
    for char in string:
        if char != ' ':
            continue
        empty_length += 2

    string += ' ' * empty_length

    index = len(string) - empty_length - 1
    index_end = len(string) - 1
    string = list(string)
    while index >= 0:
        if string[index] == ' ':
            string[index_end] = '0'
            string[index_end - 1] = '2'
            string[index_end - 2] = '%'
            index_end = index_end - 3
            index -= 1
        else:
            string[index_end] = string[index]
            index_end -= 1
            index -= 1
    return string

URLify('Mr. John Smith')

O(A)
O(A) - Memory Space

