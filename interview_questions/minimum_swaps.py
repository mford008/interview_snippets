arr = [0,2,3,4,1,6,5]

def minimumSwaps(arr):
    #Set variable to count swap number
    counter = 0
    #Set variable for length of array
    length = len(arr)
    #Create empty dictionary
    arr_dict = {}
    #For loop to create dictionary from array
    for i, item in enumerate(arr):
        arr_dict[item] = i
    #Set checked variable to false for all values in dictionary
    checked = [False]*length
    #Main loop - determine whether value has been seen previously
    for key, value in sorted(arr_dict.items(), key=lambda x: x[0]):
        #Continue if value is already in correct place
        if checked[key] or key == value:
            continue
        #Set value for cycle count
        c_count = 0
        value = key
        #If Not already checked, set to checked and increment cycle count
        while not checked[value]:
            checked[value] = True
            value = arr_dict[value]
            #Cycle count is total of points in cycle minus one
            c_count += 1
        counter += c_count - 1
    print(counter)
    return counter

minimumSwaps(arr)
