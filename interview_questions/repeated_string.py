# Set to any string
s = 'aba'

def repeatedString(s, n):
    # Set variable for length of string
    l = len(s)
    # Number of how many times the string appears in n
    multiples = n//l
    # Count how many times a appears in string
    substring_count = s.count('a')
    # Preliminary count of times a appears
    result = substring_count * multiples
    # Add number of times a appears in the remaining string letters that make up n
    result += s[:(n % l)].count('a')
    return result

repeatedString(s, 10)
