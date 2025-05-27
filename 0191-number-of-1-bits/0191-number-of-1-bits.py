class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary=bin(n)[2:]
        binary_list=[int(b) for b in binary]
        count=0
        for i in binary_list:
            if i==1:
                count+=1
        return count
        