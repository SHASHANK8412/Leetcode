class Solution:
    def reverseString(self, s: List[str]) -> None:
        #s=s.replace(" ","")
        s[:]=s[::-1]

        return s
        """
        Do not return anything, modify s in-place instead.
        """
        