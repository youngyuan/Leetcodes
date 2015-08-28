class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        res = [-1, -1]
        found = False

        #first find the target
        while low <= high:
            if not found:
                mid = low + (high - low) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    found = True
                    break

        if found:
            lefthigh = rightlow = left = right = mid
            while low <= lefthigh:
                leftmid = low + (lefthigh - low) // 2
                if nums[leftmid] == target:
                    lefthigh = leftmid - 1
                    left = leftmid
                else:
                    low = leftmid + 1

            while rightlow <= high:
                rightmid = rightlow + (high - rightlow) // 2
                if nums[rightmid] == target:
                    rightlow = rightmid + 1
                    right = rightmid
                else:
                    high = rightmid - 1
            res = [left, right]
        return res

s=Solution()
r=s.searchRange([5, 7, 7, 8, 8, 10],8)
print(r)
r=s.searchRange([3,3,3],3)
print(r)