def sherlock_and_anagrams(word):
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

# sherlock_and_anagrams('cdcd')


def count_triplets(arr, r):
    from collections import defaultdict

    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0

    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1

    return count

# count_triplets([1, 2, 2, 4], 2)


def freq_query(queries):
    from collections import Counter
    frequency = Counter()
    count = Counter()

    results = []

    for query, value in queries:

        if query == 1:
            count[frequency[value]] -= 1
            frequency[value] += 1
            count[frequency[value]] += 1

        elif query == 2 and frequency[value] > 0:
            count[frequency[value]] -= 1
            frequency[value] -= 1
            count[frequency[value]] += 1

        elif query == 3:
            if count.get(value):
                results.append(1)
            else:
                results.append(0)

    return results


# freq_query((1, 1), (1, 1), (2, 1), (3, 1))
