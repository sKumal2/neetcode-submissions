class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#check if two indices values match with the target or not and return index
#because two numbers can be anywhere, we cannot do this 

        #using a dictionary to store the index of the numbers
        seen = {}

        for i in range(len(nums)):
            potential_sum = target - nums[i]

            if potential_sum in seen:
                return [seen[potential_sum], i]
            
            seen[nums[i]] = i           
            
        