class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp0[i][j] ends in 0, dp1[i][j] ends in 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base cases: single blocks of 0s or 1s within the limit
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Transition for dp0 (ending in 0)
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i > limit:
                    dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j] + MOD) % MOD
                
                # Transition for dp1 (ending in 1)
                dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % MOD
                if j > limit:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1] + MOD) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD