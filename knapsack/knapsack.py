def maximum_value(maximum_weight, items):
    m = [[0] * (maximum_weight + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        item = items[i - 1]
        for w in range(maximum_weight + 1):
            if item["weight"] > w:
                m[i][w] = m[i - 1][w]
            else:
                m[i][w] = max(m[i - 1][w], m[i - 1][w - item["weight"]] + item["value"])

    return m[len(items)][maximum_weight]
