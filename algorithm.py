def replace_list(array, olditem, newitem):
    '''replaces occurences of olditem in integer array with newitem and returns the new array'''
    if type(array) != list:
        return False
    if type(olditem) != int:
        return False
    if type(newitem) != int:
        return False
    result = []
    for item in array:
        if item == olditem:
            result.append(newitem)
        else:
            result.append(item)
    return result
