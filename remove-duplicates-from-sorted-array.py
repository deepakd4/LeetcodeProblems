class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        while index < len(nums):
            currentnum = nums[index]
            previousnum = nums[index - 1]
            if currentnum == previousnum:
                nums.pop(index)
            else:
                index = index + 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([]))


