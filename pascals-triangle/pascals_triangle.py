def get_value(row, index):
    if index < 0 or index > len(row) - 1:
        return 0

    return row[index]


def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    if row_count == 0:
        return []

    if row_count == 1:
        return [[1]]

    previous_rows = rows(row_count - 1)
    previous_row = previous_rows[len(previous_rows) - 1]
    new_row = []
    for i in range(len(previous_row) + 1):
        new_row.append(get_value(previous_row, i - 1) + get_value(previous_row, i))

    previous_rows.append(new_row)
    return previous_rows
