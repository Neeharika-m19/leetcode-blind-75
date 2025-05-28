class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned="".join(c for c in s if c.isalnum()).lower()
        cleaned_reversed="".join(reversed(cleaned)).lower()
        if cleaned==cleaned_reversed:
            return True
        else:
            return False
        