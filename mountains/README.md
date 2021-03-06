# THE PROBLEM
Destroy the mountains before your starship collides with one of them. For that, shoot the highest mountain on your path.

# RULES
At the start of each game turn, you are given the height of the 8 mountains from left to right.
By the end of the game turn, you must fire on the highest mountain by outputting its index (from 0 to 7).

Firing on a mountain will only destroy part of it, reducing its height. Your ship descends after each pass.  

## PSEUDOCODE SOLUTION 1
1. max = First Mountain, idx = 0
2. Walk through mountains from second to last —> current
2.1. If current > max : max = current, idx = current-idx
3 Return idx

### EXAMPLE TO VALIDATE PSEUDOCODE
3, 5, 6, 7, 2, 1

Max = 3, idx = 0
Current = 5
5 > 3 ? Max = 5 , idx = 1

Current = 6
6 > 5 ? Max = 6, idx = 2

Current = 7
7 > 6 ? Max = 7, idx = 3

Current = 2
2 > 7 ? N/A

Current = 1
1 > 7 ? N/A

Return idx (3)


## PSEUDOCODE SOLUTION 2
1. MAX = 0, IDX = 0 (Validate: is it possible to have negative heights? NO in this case)
2. As we receive the values..
2.1 If (CURRENT > MAX) then MAX = CURRENT IDX = Index of CURRENT
3. Return IDX

## PSEUDOCODE SOLUTION 3
1. CREATE MAP WITH INPUT (solution works assuming all heights are different)
1.1 STORE VALUES IN LIST
2. SORT VALUES IN LIST
3, RETURN VALUE FROM MAP USING LAST VALUE IN ORDERED LIST AS KEY

    ### ALTERNATIVE IF SOME HEIGHTS REPEAT
    
    A) Create a list of indexes per height in map, height is the key.
    
    B) When the list is retrieved, delete element from list, if list is empty, delete key from MAP
    
        B.a) We could assume that altitude of the starship decreases as we destroy the mountains (thinking more in a game approach)

## ANALYSIS
### JS implementation
- Receive input, array of 'n' size -> O(1). NOTE: if we are looping to get input O(n)
- Reduce function -> O(n)
- Console log -> O(1)
Time Complexity O(n)
Time Complexity if we are looping to get heights O(2n) -> O(n)

### PYTHON implementation
- Receive input, looping to get values and create map -> O(n)
- fire() function
    ~ sort mountains -> O(n log n)
- return value from map -> O(1)
Time Complexity O(2n log n) -> O(n log n) 

