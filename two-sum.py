class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_hash:
                return [num_hash.get(complement), index]
            num_hash[num] = index


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1,2,3], 3))
