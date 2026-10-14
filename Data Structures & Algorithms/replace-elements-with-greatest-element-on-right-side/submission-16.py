class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_to_right = -1
        for i in range(len(arr)-1, -1, -1):
            max_to_right, arr[i] = max(arr[i], max_to_right), max_to_right
            
        return arr