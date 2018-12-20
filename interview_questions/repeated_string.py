# Set to any string
s = 'aba'

def repeatedString(s, n):
    l = len(s)
    multiples = n//l
    substring_count = s.count('a')
    result = substring_count * multiples
    result += s[:(n % l)].count('a')
    print(result)

repeatedString(s, 10)
