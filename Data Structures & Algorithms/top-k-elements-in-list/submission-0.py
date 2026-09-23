class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #edge cases: 
        #no elements, k is 0, k = n
        #only one unique element 
        #every element is unique 

        #basic idea: how to find most frequent element in the whole list, then find for top k elements 

        #approach : 
        #we can find most repeated like this : 
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        #now getting the max 
        '''max_num = 0
        max_frequency = 0

        for num in count:
            if count[num] > max_frequency:
                max_frequency = count[num]
                max_num = num
        '''

        #since i know, how to approach for max, how to approach for k 

        #we have the dictionary, and can sort the dict in descending order according to their values
        #then return top k frequent elements

        sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)

        #using a for loop to add just k no of elements and just the key value from the sorted_count  
        result = []
        for i in range(k):
            result.append(sorted_count[i][0])


        return result




        