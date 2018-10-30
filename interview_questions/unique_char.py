string = 'abaghyghb'

def find_char(string):
    repeats = {}
    dupes = []
    for each in string:
        if each not in repeats:
            repeats[each] = 1
        else:
            if repeats[each] == 1:
                dupes.append(each)
            repeats[each] += 1
    for each in repeats:
        if repeats[each] == 1:
            print(each)

find_char(string)
