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

def countTriplets(arr, r):
    from collections import defaultdict

    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0

    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count

countTriplets([1, 2, 2, 4], 2)
