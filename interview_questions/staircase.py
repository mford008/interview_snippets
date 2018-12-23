n = 6


def staircase(n):
    for each in range(1, n + 1):
        print(' ' * (n - each) + '#' * each)


staircase(n)
