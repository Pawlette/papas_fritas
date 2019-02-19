def fire(mountains, mountainsMap):
    size = len(mountains)
    if(size == 0):
        return -1
    mountains.sort()
    return mountainsMap[mountains[size-1]]

print("How many mountains?")
n = int(input())  # the number of mountains
mountains = []
lilMap = {}
for i in range(n):
    print "Height for ", i, ": "
    h = int(input())
    mountains.insert(i, h)
    lilMap[h] = i

print "Destroy: ", fire(mountains, lilMap)
