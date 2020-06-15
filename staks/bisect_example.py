from bisect import bisect_left, insort_left


def median(values):
    midst = len(values) // 2

    if len(values) % 2 == 0:
        return (values[midst] + values[midst - 1]) / 2
    else:
        return values[midst]


def activityNotifications(expenditure, d):
    notifications = 0
    last_d = sorted(expenditure[:d])
    for index in range(d, len(expenditure)):
        if expenditure[index] >= 2 * median(last_d):
            notifications += 1

        del last_d[bisect_left(last_d, expenditure[index - d])]
        insort_left(last_d, expenditure[index])
    return notifications
