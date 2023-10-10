from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                # Return the indices of the two numbers
                return [num_indices[complement], i]
            num_indices[num] = i  # Store the index of the current number

        return []  # Return an empty list if no target pair is found


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))

    print("________________________")

    solution2 = Solution()
    nums2 = [3, 3]
    target2 = 6
    print(solution2.twoSum(nums2, target2))


# dictionnaire valeur : target - valeur
# voir si target - valeur est dans la list

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
