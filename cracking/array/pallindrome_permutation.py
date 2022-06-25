def canPermutePalindrome(self, s: str) -> bool:
    from collections import defaultdict
    hashmap = defaultdict(int)
    for char in s:
        hashmap[char] += 1

    total = 0
    for k, v in hashmap.items():
        total += v % 2

    return total <= 1

def is_permutation_palindrome(string):
    bit = 0
    import ipdb; ipdb.set_trace()
    for char in string:
        char_ord = ord(char)

        mask = 1 << char_ord
        if (bit & mask) == 0:
            bit |= mask
        else:
            bit &= ~mask

    return (bit & (bit - 1)) == 0
