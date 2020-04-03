def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum1 = nums[0]
        temp = nums[0]

        for num in nums[1:]:
            if temp < 0:
                temp = num

                if num > maxSum1:
                    maxSum1 = num
            else:
                temp = temp + num

                if temp > maxSum1:
                    maxSum1 = temp

        return maxSum1


maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
