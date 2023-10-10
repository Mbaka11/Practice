# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        if len(strs) == 0:
            return answer
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                answer += strs[0][i]
            else:
                break
        return answer


if __name__ == "__main__":
    solution = Solution()
    strList = ["flower", "flow", "flight"]
    print("List: " + str(strList) + "\n" + "Longest Common Prefix: ")
    print(solution.longestCommonPrefix(strList))
    print("_____________________________")
    strList = ["dog", "racecar", "car"]
    print("List: " + str(strList) + "\n" + "Longest Common Prefix: ")
    print(solution.longestCommonPrefix(strList))
    print("_____________________________")
    strList = ["ab", "a"]
    print("List: " + str(strList) + "\n" + "Longest Common Prefix: ")
    print(solution.longestCommonPrefix(strList))
