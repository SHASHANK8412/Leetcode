class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        n = len(score)

        arr = []

        for i in range(n):
            arr.append((score[i], i))

        arr.sort(reverse=True)

        ans = [""] * n

        for rank in range(n):

            index = arr[rank][1]

            if rank == 0:
                ans[index] = "Gold Medal"
            elif rank == 1:
                ans[index] = "Silver Medal"
            elif rank == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(rank + 1)

        return ans