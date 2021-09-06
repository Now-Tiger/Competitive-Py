
# --------------------------------- Ordered list search ---------------------------------

def search(ordered_list, key):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if key == ordered_list[i]:
            return i
        elif ordered_list[i] > key:
            return None
    return None


if __name__ == '__main__':
    scores = [2, 3, 4, 6, 7]
    key = 5
    position = search(scores, key)

    if position is None:
        print('{} does not exist !'.format(key))
    else:
        print('{} found at position {}'.format(key, position))

    # Another example
    print('-'*30)

    key = 7
    position = search(scores, key)

    if position is None:
        print('{} does not exist !'.format(key))
    else:
        print('{} found at position {}'.format(key, position))


# $ python ordered-list-search.py
# 5 does not exist !
# ------------------------------
# 7 found at position 4
