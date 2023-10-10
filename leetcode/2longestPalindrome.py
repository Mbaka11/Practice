# Given a string s, return the longest palindromic
# substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# c b a b a d
# d a b a b c


class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        reversed = s[::-1]
        for i in range(len(s)):
            if s[i] == reversed[i]:
                answer += s[i]
                i += 1
        print(answer)
        return answer


if __name__ == "__main__":
    solution = Solution()
    string = "ababad"
    print(solution.longestPalindrome(string))
