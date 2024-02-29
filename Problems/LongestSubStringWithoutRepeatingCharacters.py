class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        sub_str = ""
        n = len(s)

        for index, c in enumerate(s):

            if c not in sub_str:
                sub_str += c

                if index != n - 1:
                    continue

            if len(result) < len(sub_str):
                result = sub_str

            index = sub_str.find(c)
            sub_str = sub_str[index + 1 :]

            sub_str += c

        return len(result)
