def reverseList(L):

    # Empty list
    if len(L) == 0:
        return

    # List with one element
    if len(L) == 1:

        # Check if that's a list
        if isinstance(L[0], list):
            return [reverseList(L[0])]
        else:
            return L

    # List has more elements
    else:
        # Get the reversed version of first list as well as the first element
        return reverseList(L[1:]) + reverseList(L[:1])





list2d = [[1,2],[3,4],[5,6],[7,8]]

list3d = [list2d, [[0,2],[3,4],[5,6],[7,8]]]

list4d = [list3d, list(reversed(list3d))]

test = reverseList(list3d)

test4 = reverseList(list4d)