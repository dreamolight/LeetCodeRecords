class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        length = len(self.nums)
        distance = j-i+1
        if not (i < length and j < length and i <= j):
            return 0

        if distance < length / 2:
            return sum(self.nums[i:j+1])
        else:
            return sum(self.nums) - sum(self.nums[0:i]) - sum(self.nums[j+1:length])