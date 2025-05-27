class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicates={}
        for num in nums:
            if num in duplicates:
                duplicates[num]+=1
            else:
                duplicates[num]=1
        for value in duplicates.values():
            if value>1:
                return True
        return False
        

        