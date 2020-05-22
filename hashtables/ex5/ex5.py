def finder(files, queries):

    """
    YOUR CODE HERE
    """
    test = {}
    result = []

    for i in files:
        file_name = i.split('/')[-1]
        if file_name in test:
            test[file_name].append(i)
        else:
            test[file_name] = [i]
    
    for i in queries:
        if i in test:
            result.extend(test[i])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
