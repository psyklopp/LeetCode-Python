'''
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12
 

Constraints: 0 <= num <= 106
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num!=0:
            if num%2 == 0:
                num = num/2
            else:
                num = num - 1
            steps += 1
        return steps

'''
Space complexity: O(1) - as we are not creating new data structures
Time complexity: O(log n) - we are halving the input - which is log n, then in worst case 
there are equal operations of subtracting 1 so.. log n + log n -> O(log n) 
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() + num.bit_count() - 1

'''
We need to remove all the ones in binary representations as well as shift one place
hence we count the number of bits - the length and the number of 1's 
We subtract one in the end because the we won't shift the 0 we get at the very last step.

Space complexity: O(1)
Time complexity: O(1) 
'''
