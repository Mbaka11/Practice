# Given an integer array nums, move all the even integers at the beginning
# of the array followed by all the odd integers.
# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        temp = nums.copy()
        for elem in nums:
            print(elem)
            if elem % 2 == 0:
                print("EVEN", elem)
                answer.append(elem)
                temp.remove(elem)

        answer.extend(temp)
        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 1, 2, 4]
    print(solution.sortArrayByParity(nums))
