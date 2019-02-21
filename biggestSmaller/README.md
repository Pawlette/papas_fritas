# The Biggest Smaller Number

## The problem
Given a number, find and return its biggest smaller number
This problem was given to me in a job interview, i loved it! Simple, yet quite entertaining

### Example 1
Suppose you're given the following number: 37,153 ..which number can you create using the same digits, which is smaller than it, but the next biggest one.

Input: 37,153

Output: 37,135

### Example 2
Input: 11,230

Output: 11,203

### Example 3
Input: 809,179

Oputput: 807,991


## Solution (From Left to Right)
### Assumptions 
- The number has 'n' number of digits
- i for index starting from 0 (zero)
- TemporaryResult = 0

1. Walk through the digits of the given number from Left to Right, starting from position zero i=0
2. Is there any smaller digit than me in the following positions? (i+1 TO n-1)?

   2.a No, then move to step 3 (Move to next digit)
   
   2.b Yes, switch numbers, then from following position to n, order digits in descending order
   
       2.b.1 Attach ordered digits to currentResult
       2.b.2 If currentResult is bigger than temporary result, assign value to temporary result
       
3. Repeat from step 1, increase index (i += 1)

4. Return temporary result

## Solution (From Right to Left)
Be elegant and impress!!! ;)

### Assumptions
- The number has 'n' number of digits
- i for index starting from 0 (zero)
- TemporaryResult = 0

1. Start from digit at last position in number i = (n-1)
2. Find any digit in the previous positions (0 TO (i-1)) bigger than current digit (PLEASE NOTE: NOT EQUALS)

    2.a Did you find it?
    
        2.a.1 Then, switch digits, and from the next position of the value you found to (n-1), order digits in descending order
        2.b.2 Attach ordered digits to result after switching digits
        2.b.3 Return result
    2.b No?
    
        2.b.1 Then, move to previous digit
3. Repeat from step 2
4. Return TemporaryResult

