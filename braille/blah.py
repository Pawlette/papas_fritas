class Alph:
    list = []
    binaries = []

    def __init__(self):
        self.list = [[2,0,0],[2,2,0],[3,0,0],[3,1,0],[2,1,0],[3,2,0],[3,3,0],[2,3,0],[1,2,0],[1,3,0],[2,0,2],[2,2,2],[3,0,2],[3,1,2],[2,1,2],[3,2,2],[3,3,2],[2,3,2],[1,2,2],[1,3,2],[2,0,3],[2,2,3],[1,3,1],[3,0,3],[3,1,3],[2,1,3],[0,0,0],[0,0,1]]
        self.binaries = [[0,0],[0,1],[1,0],[1,1]]

def solution(s):
    solution = ""
    if (not isinstance(s, str)):
        return solution

    if (len(s) > 50):
        return solution

    # Your code here
    dicc = Alph()

    # ascii references to map to Alphabet
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    upper = ord('_')
    space = 32 # blank space

    chars = []
    # iterate chars through string to find UpperCase
    for c in s:
        char_int = ord(c)
        if (char_int >=A and char_int <= Z):
            chars.append('_')
            chars.append(c)
        elif (char_int >= a and char_int <= z):
            chars.append(c)
        elif (char_int == space):
            chars.append(c)

    # Holds the result
    braille = [ 0 for y in range(len(chars)*6) ]

    x = 0 
    for c in chars:
        char_int = ord(c)
        if (char_int == space):
            char_idx = 26 # In the dicc, the blank space is in location 26
        elif (char_int >= a and char_int <= z):
            char_idx = char_int - a
        elif (char_int >=A and char_int <= Z):   
            char_idx = char_int - A
        elif (char_int == upper):
            char_idx = 27 # in dicc, underscore defines UpperCase
            
        limit = 0
        begin = (x * 6)
        while(limit < 3):
            # Gets the braille value for char in alphabet
            braille_value = dicc.list[char_idx]
            # decomponse to binaries
            decimal = braille_value[limit]
            binary = dicc.binaries[decimal]

            braille[begin] = binary[0]
            braille[begin+3] = binary[1]
            
            limit += 1 
            begin += 1
        x += 1 # move to next char
    
    solution = ''.join([str(elem) for elem in braille])
    print('Solution for', s, ' is:', solution)
    return solution 

solution("Braille")
solution('A^&_1z')
solution("A")
solution("a")
solution(1)
solution(" ")
solution("The quick brown fox jumps over the lazy dog")
