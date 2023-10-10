class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        answer = 0
        index = 0

        while (index < len(s)):
            if index + 1 < len(s) and roman_numbers_dict[s[index]] < roman_numbers_dict[s[index + 1]]:
                answer -= roman_numbers_dict[s[index]]
            else:
                answer += roman_numbers_dict[s[index]]

            index += 1
        return answer


if __name__ == "__main__":
    test = Solution()
    answer = test.romanToInt("MCMXCIV")
    print(answer)

# LVIII  58
# MCMXCIV 1994
