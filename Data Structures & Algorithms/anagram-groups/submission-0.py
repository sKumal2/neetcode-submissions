class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we need to group anagrams 
        #anagrams can be from the same word or different words
        #edge cases: empty input, no anagrams, duplicate strings, different lengths 

        #basic way of finding anagrams : 
        #use a dictionary and count how many times each letter is repeated in the word

        #creating a dictionary to add all the anagrams in one place
        groups = {}

        #creating a key for each value from the list to dictionary
        for word in strs:
            key = "".join(sorted(word))

            #add the keys to the group if not already
            if key not in groups:
                groups[key] = []

            #append all the words, not keys to the groups key
            groups[key].append(word)

#just return the values in a dictionary, not the keys but as a list
        return list(groups.values())
