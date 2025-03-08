class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的 left 和 right
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
                elif total < 0:
                    left +=1
                else:
                    right -=1
        return res