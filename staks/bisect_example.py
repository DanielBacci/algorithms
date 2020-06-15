from bisect import bisect_left, insort_left


def median(values, d):
    if d % 2 == 1:
        return values[d // 2]
    return (values[d // 2] + values[d // 2 - 1]) / 2


def activityNotifications(expenditure, d):
    notifications = 0
    last_d = sorted(expenditure[:d])
    for index in range(d, len(expenditure)):
        if expenditure[index] >= 2 * median(last_d, d):
            notifications += 1

        del last_d[bisect_left(last_d, expenditure[index - d])]
        insort_left(last_d, expenditure[index])
    return notifications
