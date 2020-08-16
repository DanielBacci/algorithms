def commonChild(s1, s2):
    # based on LCS algorithm
    n = len(s1)
    preview_row = [0] * (n + 1)
    current_row = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                current_row[j] = preview_row[j - 1] + 1
            else:
                if current_row[j - 1] >= preview_row[j]:
                    current_row[j] = current_row[j - 1]
                else:
                    current_row[j] = preview_row[j]
        preview_row = current_row
        current_row = [0] * (n + 1)
    return preview_row[n]

commonChild("ABCD", "ABDC")
