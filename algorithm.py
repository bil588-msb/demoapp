def replace_list(array, olditem, newitem):
    '''replaces occurences of olditem in integer array with newitem and returns the new array'''
    result = None
    if type(array) == list:
        result = []
        for item in array:
            if item == olditem:
                result.append(newitem)
            else:
                result.append(item)
    return result
