def riddle(arr):
    maximum = [0] * len(arr)

    for i in range(0, len(arr)):
        right = i
        left = i

        while right + 1 < len(arr) and arr[right + 1] >= arr[i]:
            right += 1

        while left - 1 >= 0 and arr[left - 1] >= arr[i]:
            left -= 1

        for j in range(right - left + 1):
            maximum[j] = max(maximum[j], arr[i])

    return maximum
