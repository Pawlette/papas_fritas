def findBiggestSmallerRightToLeft(num):
    digits = [int(d,10) for d in str(num)]
    if(len(digits) == 1):
        return num
    if(len(digits) == 2):
        if(digits[1] < digits[0]):
            tmp = digits[0]
            digits[0] = digits[1]
            digits[1] = tmp
        return int("".join(map(str, digits))) 

    # Get last digit from number
    last = len(digits)-1
    pivot = -1
    while(last > 1):
        current = digits[last]
        for i in range(last-1, -1, -1):
            if(digits[i] > current):
                tmp = digits[i]
                digits[i] = current
                digits[last] = tmp
                pivot = i
                last = 0
                break
        last -= 1
    if(pivot > 0):
        result = []
        for i in range(0, pivot+1):
            tmp = digits.pop(0)
            result.append(tmp)
        digits.sort(reverse=True)
        result += digits
        return int("".join(map(str, result)))    
    else:
        return pivot
   
num = 809179
#num = 11230
#num = 37153
print "Input: ", num
output = findBiggestSmallerRightToLeft(num)
print "Result is: ", output
