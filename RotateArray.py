class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 0 or k <= 0:
            return

        i = 0
        pos = 0
        start_pos = 0
        prev = nums[0]
        while True:
            new_pos = (pos + k) % n
            current = nums[new_pos]
            nums[new_pos] = prev

            # check if all elements are set
            i += 1
            if i >= n:
                return

            prev = current
            pos = new_pos

            if pos == start_pos:
                start_pos += 1
                pos = start_pos
                prev = nums[pos]

s = Solution()
r = [1, 2, 3, 4, 5, 6, 7]
s.rotate(r, 3)
print(r)
r = [1, 2, 3, 4, 5, 6]
s.rotate(r, 2)
print(r)
r = [1, 2, 3, 4, 5, 6]
s.rotate(r, 1)
print(r)
r = [1]
s.rotate(r, 1)
print(r)