def has_negatives(a):

    """
    YOUR CODE HERE
    """
    #Convert array to dict with indexes as value
    arr = dict(map(reversed, enumerate(a)))
    result = {}
    
    for key_i in arr:
        index = 0
        for key_j in arr:
         
            index += 1   
            
            if key_i + key_j == 0:
                if key_i > 0:
                    key = key_i
                else:
                    key = key_j
                # print(key)
                result[key] = abs(key)
            
            
    # print(result)

    return list(result)








if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
