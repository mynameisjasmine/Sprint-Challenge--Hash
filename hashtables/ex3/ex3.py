from collections import Counter

def intersection(arrays):

    """
    YOUR CODE HERE
    """
    #changing the array of arrays to a dict, with the indexes as keys and the arrays as values
    dict_list = {}

    for i in arrays:
        dict_list[i[0]] = i[0:]
        return dict_list


    
    # arrays = Counter(arrays)
    # new_hash = dict(arrays.items())
    # result = []

    # for (key, val) in new_hash.items():
    #     for i in range(0, val):
    #         result.append(key[i])

    # return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
