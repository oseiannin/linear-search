def linear_search(array, te):
    """return a boolean of the presence status of te"""
    for element in array:
        if compare(element, te):
            return True
    return False


def compare(item_one, item_two):
    """returns true if two args are the same and false otherwise"""
    if item_one == item_two:
        return True
    return False


if __name__ == '__main__':
    search_one = linear_search([1, 23, 3, 4, 5], 3)  # true
    search_two = linear_search([32, 4, 3, 532, 5], 100)  # false

    print(search_one, "-----", search_two)
