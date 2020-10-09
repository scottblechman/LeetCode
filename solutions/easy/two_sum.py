from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    if len(nums) == 2:
        return [0, 1]
    for x in range(0, len(nums)):
        subtrahend = target - nums[x]
        if subtrahend in nums and nums.index(subtrahend) != x:
            return [x, nums.index(subtrahend)]
