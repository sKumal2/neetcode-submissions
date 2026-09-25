class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #using two pointers algorithm, sort the list so i can use it efficiently 
        #edge cases: no three sums 

        nums.sort()
        result = []
        for i in range(len(nums)):
    #this works but need to handle the duplicate set of items
            if i > 0 and nums[i] == nums[i -1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    #Increase left pointer and decrease right pointer
                    left += 1
                    right -= 1

                    #handles duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif current_sum < 0:
                    left += 1

                else:
                    right -= 1

        return result




