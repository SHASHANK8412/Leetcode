class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [n] * n

        # Pass 1: left -> right, distance from the nearest c seen so far
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # Pass 2: right -> left, take the smaller distance from the nearest c ahead
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)

        return answer