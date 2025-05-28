class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(n+1):
            count=0
            binary=bin(i)[2:]
            for b in binary:
                if b=='1':
                    count+=1
            ans.append(count)
        return ans
        