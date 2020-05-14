def has_negatives(a):
    # set empty result list, negative and positive empty dict
    result = []
    negative = {}
    positive = {}
    # iterate through items and assign to positive or negative dict
    for i in a:
        if i < 0:
            negative[i] = i*-1
        else:
            positive[i] = i
    # iterated through and append positive items
    for i in negative.values():
        if i in positive:
            result.append(positive[i])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
