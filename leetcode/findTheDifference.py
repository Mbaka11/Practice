# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
# Input: s = "abcd", t = "abcde"
# Output: "e"

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seenletters = []
        for i in t:
            seenletters.append(i)
        for i in s:
            if i in seenletters:
                seenletters.remove(i)
        return "".join(seenletters)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheDifference("abcd", "adbce"))
    print(solution.findTheDifference("a", "aa"))
