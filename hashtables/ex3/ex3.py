def intersection(arrays):
    # start empty result list and empty dictionary
    result = []
    d = {}
    # iterated through array and append keys
    for i in arrays:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    for key in d.keys():
        if d[key] == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
