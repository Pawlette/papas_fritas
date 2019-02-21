def findBiggestSmallerRightToLeft(num):
    # Get Digits from number
    digits = [int(d,10) for d in str(num)]
    # The first two basic cases, the number has one or two digits
    if(len(digits) == 1):
        return num
    if(len(digits) == 2):
        if(digits[1] < digits[0]):
            tmp = digits[0]
            digits[0] = digits[1]
            digits[1] = tmp
        return int("".join(map(str, digits))) 

    # Get the biggest number
    ordered = [int(d,10) for d in str(num)]
    ordered.sort(reverse=True)
    biggestNum = ordered[0]

    i = len(digits) - 1
    pivot = -1
    while (i > 0 and pivot < 0):
        current = digits[i]
        if(current < biggestNum):
            j = i - 1
            while(j >= 0 and pivot < 0):
                if(digits[j] > current):
                    tmp = digits[j]
                    digits[j] = current
                    digits[i] = tmp
                    pivot = j
                j -= 1
        i -= 1

    result = 0
    j = len(digits) - 1
    for i in range(0, pivot+1):
        d = digits.pop(0)
        result += pow(10, j) * d
        j -= 1

    digits.sort(reverse=True)
    for d in digits:
        result += pow(10, j) * d
        j -= 1
    return result

# TESTING #
num = 89
print "Input: ", num
output = findBiggestSmallerRightToLeft(num)
print "Result is: ", output

num = 65
print "Input: ", num
output = findBiggestSmallerRightToLeft(num)
print "Result is: ", output

num = 809179
print "Input: ", num
output = findBiggestSmallerRightToLeft(num)
print "Result is: ", output

num = 71805058
print "Input: ", num
output = findBiggestSmallerRightToLeft(num)
print "Result is: ", output

num = 70058888
print "Input: ", num
output = findBiggestSmallerRightToLeft(num)
print "Result is: ", output

#num = 11230
#num = 37153