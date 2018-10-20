array = [2, 3, 4, 6, 7, 9]
total = 10

def find_pairs(array, total):
    count = 0
    length = len(array)
    for i in range(0, length):
        for j in range(i + 1, length):
            if array[i] + array[j] == total:
                count += 1
                print(array[i], array[j])
    print(count)
    return count

find_pairs(array, total)
