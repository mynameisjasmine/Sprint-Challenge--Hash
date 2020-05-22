from collections import Counter

def intersection(arrays):

    """
    YOUR CODE HERE
    """

    arrays.sort(key=lambda s:len(s))
    result = []
    arr_obj = {}

    for y, i in enumerate(arrays):
        for i in i:
            if i in arr_obj:
                arr_obj[i].append(i)
            elif y == 0:
                arr_obj[i] = [i]

    for index, value in arr_obj.items():
        if len(value) == len(arrays):
            result.append(index)



    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
