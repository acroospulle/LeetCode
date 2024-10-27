class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time - O(n)  space - O(n)
         hashset = set()

         for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
         return False
        