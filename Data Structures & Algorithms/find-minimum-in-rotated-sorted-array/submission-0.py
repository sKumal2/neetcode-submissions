class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we can find minumum easily in O(n) time using bruteforce 
        #but we need O(logn) time, so using binary search 

        l, h = 0, len(nums) - 1

        while l < h:

            mid = l + (h - l) // 2 

            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid

        return nums[l]
         
