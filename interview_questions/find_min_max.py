unsorted = [5, 3, 8, 1, 2, 4]

def find_min_max(unsorted):
    # largest = unsorted[0]
    lowest = unsorted[0]
    for number in unsorted:
        # if number > largest:
        #     largest = number
        if number < lowest:
            lowest = number
    # print(largest)
    print(lowest)
find_min_max(unsorted)
