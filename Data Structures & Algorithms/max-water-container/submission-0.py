class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #the problem asks us to find the max area 
        #for area we need width and height
        #we can use two pointers approach
        #if the height is more then move forward, and save max area, return max area 
        #edge cases : 
        #max area cant be from tallest two lines, so we save max area 
        #duplicate heights; so calculate min, and save it and move the pointer 


        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            area = width * height 

            if area > max_area:
                max_area = area

            #moving the pointers 
            if heights[left] > heights[right]:
                right -= 1 
            else:
                left += 1

        return max_area