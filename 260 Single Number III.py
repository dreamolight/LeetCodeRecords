class Solution(object):
    def XORList(self, nums):
        xor = 0

        length = len(nums)
        for i in range(0,length):
            xor = xor ^ nums[i]

        return xor

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = self.XORList(nums)

        rightmost = xor & ~(xor - 1)

        left_list = [x for x in nums if x & rightmost == 0]
        right_list = [x for x in nums if x & rightmost != 0]

        return [self.XORList(left_list),self.XORList(right_list)]


sol = Solution()
print sol.singleNumber([1,2,3,1,2,5])