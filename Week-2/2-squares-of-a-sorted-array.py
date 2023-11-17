'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

1 <= nums.length <= 10^4

-10^4 <= nums[i] <= 10^4

nums is sorted in non-decreasing order.
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        start = 0
        end = length - 1
        ans = []
        ans_final = []
        while start <= end:
            if nums[start]*nums[start] >= nums[end]*nums[end]:
                ans.append(nums[start]*nums[start])
                start += 1
            else:
                ans.append(nums[end]*nums[end])
                end -= 1
        length -= 1
        while length>=0:
            ans_final.append(ans[length])
            length -= 1
        return ans_final
    
'''
Space Complexity: O(1) - We are not adding new data structures as the input grows
Time Complexity: O(N) - We iterate for n-numbers and append takes O(1)
'''