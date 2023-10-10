# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        addition = 0

        while n != 1:
            if n in seen_numbers:
                return False
            seen_numbers.add(n)
            for digit in str(n):
                addition += int(digit) ** 2
            n = addition
            addition = 0

        return True


if __name__ == "__main__":
    solution = Solution()
    solution.isHappy(19)
    print(solution.isHappy(19))
    print("_____________________________")
    print(solution.isHappy(2))
    print("_____________________________")
    print(solution.isHappy(7))
    print("_____________________________")
    print(solution.isHappy(1111111))
    print("_____________________________")
