def get_indices_of_item_weights(weights, length, limit):

    w_dictionary = {}
    for k, v in enumerate(weights):
        if v in w_dictionary:
            w_dictionary[v].append(k)
        else:
            w_dictionary[v] = [k]
    for i, w in enumerate(w_dictionary):
        if limit-w in w_dictionary:
            if w_dictionary[limit-w] is w_dictionary[w]:
                if len(w_dictionary[w]) >= 2:
                    return (w_dictionary[limit-w][1], w_dictionary[w][0])
            else:
                return (w_dictionary[limit-w][0], w_dictionary[w][0])

    return None
