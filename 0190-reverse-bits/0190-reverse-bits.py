class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary=format(n,'032b')
        reversed_bin=binary[::-1]
        num=int(reversed_bin,2)
        return num
        