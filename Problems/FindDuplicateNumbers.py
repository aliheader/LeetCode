from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return num
            
            duplicate.add(num)