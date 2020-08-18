import math 
def find_pivot_point(arr):
  if len(arr) == 2:
    if arr[0] > arr[1]:
      return 1
    else:
      return 0
  left = 0
  right = len(arr) - 1
  last_changed = left
  
  while(left != right):
    mid_idx = math.floor((left + right)/2)
    mid_value = arr[mid_idx]
    
    if mid_value < right:
      right = mid_idx - 1
      last_changed = right 
    else:
      left = mid_idx + 1 
      last_changed = left
  
  return last_changed
# print(find_pivot_point([5,6,7,8,0,1,2]))


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_pivot_point(arr):
          if len(arr) == 2:
            if arr[0] > arr[1]:
              return 1
            else:
              return 0
          left = 0
          right = len(arr) - 1
          last_changed = left

          while(left != right):
            mid_idx = math.floor((left + right)/2)
            mid_value = arr[mid_idx]

            if mid_value < right:
              right = mid_idx - 1
              last_changed = right
            else:
              left = mid_idx + 1
              last_changed = left

          return last_changed

        self.pivot_idx = find_pivot_point(nums)

        def rotated_b_search(nums, target):
            left = 0
            right = len(nums)-1
            while(left != right):
                mid_idx = math.floor((left + right) / 2)
                middle_value = nums[mid_idx-(self.pivot_idx-1)]

                if middle_value == target:
                    return pivot_idx - 1
                elif middle_value > target:
                    right = mid_idx - 1
                else:
                    left = mid_idx + 1
            if nums[left-(self.pivot_idx-1)] == target:
                idx = left-(self.pivot_idx-1)
                if idx < 0: 
                  return len(nums) + idx
                else:
                  return idx
            else:
                return -1
        return rotated_b_search(nums, target)

solution = Solution()
# print(solution.search([4, 5, 6, 7, 0, 1, 2],0))
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
print(solution.search([0, 1, 2], 3))
