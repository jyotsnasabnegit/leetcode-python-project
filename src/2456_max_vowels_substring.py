class Solution():
    def maxSubstring(self,s, k):
        vowels = "aeiou"
        i= 0
        j= 0
        maxCount = 0
        count = 0

        for j in range(0, len(s)):
            if(s[j] in vowels):
                count += 1
            
            if((j-i) >= k):
                if(s[i] in vowels):
                    count -= 1
                i += 1
        
            maxCount = max(maxCount, count)
        
        return maxCount

print(Solution().maxSubstring("abciiidef",3))
