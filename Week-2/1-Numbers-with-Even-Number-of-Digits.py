'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''

# Divide the number by 10 to get digits and count

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for num in nums:
            digits = 0
            while num > 0:
                num = int(num/10)
                digits = digits + 1
                print(num)
            if digits % 2 == 0:
                even = even + 1
        return even

# Convert to string and count the length -- faster

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for num in nums:
            if len(str(num))%2 == 0:
                even += 1
        return even
    
# Take the log base of 10 + 1

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
	    # We are going to take advantage of the fact that the array only contains positive integers.
		# A common formula for finding the number of digits in a positive number is digits = floor(log10(num)) + 1
		# Even if the array contained negatives, you could just do the same with the absolute value of num.
		# This turns the runtime into O(N) and there is no additional space needed so O(1) space.
		# You also don't need to convert this into a string which a lot of other solutions do and has other implications in terms of space complexity.
		# https://brilliant.org/wiki/finding-digits-of-a-number/
        result = 0
        
        for num in nums:
            num_digits = floor(log10(num)) + 1
            if num_digits % 2 == 0:
                result += 1
                
        return result
