# Python3 solution to Sock Merchant problem on Hackerrank
socks = [1,2,1,2,1,3,2]

def totalPairs(socks):
    # Create empty dictionary
    pairs = {}
    # Loop through array
    for each in socks:
        if each not in pairs:
            # Establish new key value pair for new keys
            pairs[each] = 1
        else:
            # Increment previously added values
            pairs[each] += 1
    # Loop through pairs dictionary
    for each in pairs:
        # Divide by two and round down for each value to represent sock pairs
        pairs[each] = pairs[each]//2
        # Sum total of dictionary - total number of pairs
        total = sum(pairs.values())
    return total
totalPairs(socks)
