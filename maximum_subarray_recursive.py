def maxSubArray(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  def recursiveFunct(subArr):
      if len(subArr) == 1:
          return [subArr[0], subArr[0]]

      largestSumArr = recursiveFunct(subArr[0:len(subArr)-1])

      if largestSumArr[0] < 0:
          if subArr[-1] > largestSumArr[1]:
            largest = subArr[-1]
          else:
            largest = largestSumArr[1]
          return [subArr[len(subArr)-1], largest]
      else:
          sum = largestSumArr[0] + subArr[len(subArr)-1]
          if sum > largestSumArr[1]:
            largest = sum
          else:
            largest = largestSumArr[1]

          return [sum,largest]

  return recursiveFunct(nums)[1]


# print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
