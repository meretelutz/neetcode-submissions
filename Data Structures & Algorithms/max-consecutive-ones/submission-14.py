class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:        
        # streaks = [0]
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         streak = 1
        #         for j in range(i+1, len(nums)):
        #             if nums[j] == 1:
        #                 streak += 1
        #             else:
        #                 break
        #         streaks.append(streak)
        
        # return max(streaks)

        # max_streak, current_streak = 0, 0
        # for num in nums:
        #     if num == 1:
        #         current_streak += 1
        #     else:
        #         if current_streak > max_streak:
        #             max_streak = current_streak
        #             current_streak = 0
        #         else:
        #             current_streak = 0
        # return max(max_streak, current_streak)

        max_streak = current_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
            else:
                current_streak = 0
            max_streak = max(max_streak, current_streak)
                
                
        return max_streak

