def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
print(twoSum(twoSum, [11,10,2,7], 9))
