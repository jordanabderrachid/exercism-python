def transform(legacy_data):
    new_data = {}
    for point in legacy_data:
        for l in legacy_data[point]:
            new_data[l.lower()] = point

    return new_data
