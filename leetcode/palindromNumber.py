class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        x_reverse = x_str[::-1]

        return x_str == x_reverse


if __name__ == "__main__":
    solution = Solution()
    number = 100001
    print(solution.isPalindrome(number))

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left
