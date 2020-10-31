# Mapping tables
alphabet = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
braille_ = [
'000000',
'100000',
'110000',
'100100',
'100110',
'100010',
'110100',
'110110',
'110010',
'010100',
'010110',
'101000',
'111000',
'101100',
'101110',
'101010',
'111100',
'111110',
'111010',
'011100',
'011110',
'101001',
'111001',
'010111',
'101101',
'101111',
'101011']

def solution(s):
    result=""

    if (not isinstance(s, str)):
        return result

    if (len(s) > 50):
        return result
	
    for i in range(len(s)):
        if s[i].isupper(): # validate is upper case
            result = result + '000001' # uppercase wildcard

        # Element is a valid char in Alphabet
        if s[i].lower() in alphabet:
            result = result + braille_[alphabet.index(s[i].lower())]
    print('Solution for: ', s, ' is: ' + result)
    return result

solution("A")
solution("a")
solution(1)
solution(" ")
solution("code1")
