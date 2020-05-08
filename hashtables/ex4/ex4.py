def has_negatives(a):

    """
    YOUR CODE HERE
    """
    #Convert array to dict with indexes as value
    new_one = dict(map(reversed, enumerate(a)))
    result = []
     
     if key in new_one.keys():
    

    return result



# def find_pairs (arr):

# check = len(arr)
# pos_int = []
# for i in range(check):
    
#     for j in range(i + 1, check):
#         if abs(arr[i]) == abs(arr[j]):
#             v.append(abs(arr[i]))
#             # v.append(abs(arr[j]))
        


#             return pos_int



if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
