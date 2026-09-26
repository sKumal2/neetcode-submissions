class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #edge case: not present 
        #we can easily search the target in O(n) time using bruteforce but the main requirement is O(logn) time 
        #we could even try sorting first and doing binary search, requires O(nlogn) time, which doesn't meet target 
        
        #since it is rotated, we need binary search

        l, h = 0, len(nums) - 1

        while l <= h:
            mid = l + (h - l) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1

        return -1
            
