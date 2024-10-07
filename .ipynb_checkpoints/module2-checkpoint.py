list1 = [5, 10, 15, 20, 25]
list2 = [1, 2, 3, 4, 5]
list3 = [9, 8, 7, 6, 5]
list4 = [100, 200, 300, 400, 500]


def get_list(list_name):
    """Returns a list of integers based on the list name."""

    if list_name == "list1":
        return list1
    elif list_name == "list2":
        return list2
    elif list_name == "list3":
        return list3
    elif list_name == "list4":
        return list4
    else:
        return "List not found"
