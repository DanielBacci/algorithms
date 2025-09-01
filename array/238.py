def product_except_self(numbers):

    acc_pre = 1
    cache_result = []
    for index, number in enumerate(numbers):
        cache_result.append(acc_pre)
        acc_pre *= number

    acc_pos = 1
    n = len(numbers)
    for i, number in enumerate(reversed(numbers)):
        original_index = n - 1 - i
        cache_result[original_index] *= acc_pos
        acc_pos *= numbers[original_index]

    return cache_result
