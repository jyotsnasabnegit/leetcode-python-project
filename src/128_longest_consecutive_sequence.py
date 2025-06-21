class Solution(object):
    def longestConsecutive(self, nums):
        mySet = set(nums)

        longestSequence = 0
        for num in mySet:
            if num - 1 not in mySet:
                currNum = num
                currSeq = 1

                while currNum + 1 in mySet:
                    currNum += 1
                    currSeq += 1
                
                longestSequence = max(longestSequence, currSeq)
        
        return longestSequence