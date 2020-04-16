def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    diffH = {0: -1}
    counts = [0, 0]
    longest = 0

    for idx in range(len(nums)):
      counts[nums[idx]] += 1
      diff = counts[0] - counts[1]

      if diff not in diffH:
        diffH[diff] = idx
      else:
        curr = idx - diffH[diff]

        if curr > longest:
          longest = curr

    return longest
    
findMaxLength([0,1,0,1])