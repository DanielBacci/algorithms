def max_combination(nums):
    max_amount = 0
    loop_amount = 0
    negative_index = None
    index = 0

    while index < len(nums):
        if nums[index] >= 0:
            loop_amount += nums[index]
            max_amount = max(max_amount, loop_amount)
            index += 1

        elif negative_index is None:
            loop_amount += nums[index]
            max_amount = max(max_amount, loop_amount)
            negative_index = index
            index += 1

        else:
            loop_amount = 0
            index = negative_index + 1
            negative_index = None

    return max_amount
