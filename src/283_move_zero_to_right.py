class Solution():
    def test(self, nums):
        i = 0
        j = 0
        length = len(nums)
        print(length)

        while i < length:
            if nums[i] == 0 and nums[j] == 0:
                j = j + 1
                print(i, j)
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j + 1
                print(i, j)

        return nums  
    
print(Solution().test([4,0,0,0,0,3,2,5,1,4]))
