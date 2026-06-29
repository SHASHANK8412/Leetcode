class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = n & 1        # Extract last bit
            ans = ans << 1     # Make space
            ans = ans | bit    # Place extracted bit
            n = n >> 1         # Remove last bit

        return ans