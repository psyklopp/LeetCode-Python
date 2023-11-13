'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Question: https://leetcode.com/problems/ransom-note/
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter()
        for ch in magazine:
            c[ch] += 1
        for ch in ransomNote:
            if c[ch] == 0:
                return False
            else:
                c[ch] -= 1
        return True

#   One liner solution

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)
    
'''
Space Complexity: O(1) most probably - as we don't create new data structures as input grows
Time Complexity: O(N+M) --> O(N) as counter is a sub-class of dict and just iterates over the characters ones
'''
