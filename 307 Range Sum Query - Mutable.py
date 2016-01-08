class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sum = 0
        self.old_i = 0
        self.old_j = 0

        self.summed = False
        
    def update(self, i, val):
        old = self.nums[i]
        self.nums[i] = val
        self.sum = self.sum + val - old

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.summed and self.old_i == i and self.old_j == j:
            return self.sum
        
        self.summed = True
        self.old_i = i
        self.old_j = j

        length = len(self.nums)
        distance = j-i+1
        if not (i < length and j < length and i <= j):
            self.sum = 0
            return 0

        if distance < length / 2:
            self.sum = sum(self.nums[i:j+1])
            return self.sum
        else:
            self.sum = sum(self.nums) - sum(self.nums[0:i]) - sum(self.nums[j+1:length])
            return self.sum