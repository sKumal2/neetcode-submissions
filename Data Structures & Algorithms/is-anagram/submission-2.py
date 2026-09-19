class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #have to be the same no of times, using a dict to count how many times each word repeats
        if len(s) != len(t):
            return False

            
        count = {}
        #this helps count how many times each letter is present in the count dict
        for i in s:
            #give me the current value of i, if not use 0 and then increase the count by 1 
            count[i] = count.get(i, 0) + 1

#now compare each word if it is in count or not, and exactly how many times
        for i in t:
            if i not in count:
                return False
            
            count[i] -= 1

            if count[i] < 0:
                return False   

        return True

        


        