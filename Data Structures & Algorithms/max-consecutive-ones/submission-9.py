class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:        
        streaks = [0]
        for i in range(len(nums)):
            if nums[i] == 1:
                streak = 1
                for j in range(i+1, len(nums)):
                    if nums[j] == 1:
                        streak += 1
                    else:
                        break
                streaks.append(streak)
        
        return max(streaks)

