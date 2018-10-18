a = [1, 2, 3, 4, 6, 6, 3, 7]
seen = {}
dupes = []

for x in a:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1
print(seen)
print(dupes)
