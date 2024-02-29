class Solution:
    def partitionString(self, s: str) -> int:
        result = 1
        sub = ""

        for c in s:
            if c not in sub:
                sub += c
                continue

            result += 1
            sub = c

        return result
