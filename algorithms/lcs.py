def commonChild(s1, s2):
    # based on LCS algorithm
    n = len(s1)
    preview_row = [0] * (n + 1)
    current_row = [0] * (n + 1)
    for index in range(1, n + 1):
        for index_s2 in range(1, n + 1):
            if s1[index - 1] == s2[index_s2 - 1]:
                current_row[index_s2] = preview_row[index_s2 - 1] + 1
            else:
                if current_row[index_s2 - 1] >= preview_row[index_s2]:
                    current_row[index_s2] = current_row[index_s2 - 1]
                else:
                    current_row[index_s2] - preview_row[index_s2]

        preview_row = current_row
        current_row = [0] * (n + 1)

    return preview_row[n]
