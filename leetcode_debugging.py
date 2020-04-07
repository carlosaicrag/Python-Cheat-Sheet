def countElements(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict = {}
        set = {}
        count = 0

        for num in arr:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for num in dict:
            if num + 1 in dict:
                if dict[num + 1] != 0:
                    count += 1

        return count


countElements([1,2,3])
