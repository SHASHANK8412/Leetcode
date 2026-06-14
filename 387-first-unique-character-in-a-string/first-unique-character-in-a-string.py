class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = {}

        # Count frequency of each character
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # Find first character with frequency 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1