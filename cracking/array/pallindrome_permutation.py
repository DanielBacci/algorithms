    def canPermutePalindrome(self, s: str) -> bool:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1

        total = 0
        for k, v in hashmap.items():
            total += v % 2

        return total <= 1
