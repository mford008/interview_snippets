def getCount(inputStr):
    num_vowels = 0
    for each in inputStr:
        if each in 'aeiouAEIOU':
            num_vowels += 1
    print(num_vowels)

getCount('grumpycat')
