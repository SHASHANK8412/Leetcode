class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        # Step 1: Build Prefix Sum Array
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        total = prefix[n - 1]

        # Step 2: Check each index
        for i in range(n):

            if i == 0:
                left = 0
            else:
                left = prefix[i - 1]

            right = total - prefix[i]

            if left == right:
                return i

        return -1