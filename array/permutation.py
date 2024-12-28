def permutation(string_1, string_2):
    NO_OF_CHARS = 256
    chars = [0] * NO_OF_CHARS

    if len(string_1) != len(string_2):
        return False

    index = 0
    while index <= len(string_1) - 1:
        chars[ord(string_1[index])] += 1
        chars[ord(string_2[index])] -= 1
        index += 1

    for char in chars:
        if char != 0:
            return False
    return True

permutation("bacci", "bacci")


O(n + 128) => O(n)
O(n) => Memory Space
