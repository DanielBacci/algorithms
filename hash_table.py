def sherlockAndAnagrams(word):
    from collections import defaultdict

    items = defaultdict(int)
    length = len(word)
    for i in range(length):
        for j in range(i, length):
            item = word[i:j + 1]
            items[''.join(sorted(item))] += 1

    total = 0
    for _, value in items.items():
        total += (value * (value - 1)) // 2

    return total

sherlockAndAnagrams('cdcd')
