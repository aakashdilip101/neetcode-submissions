class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        current_sublist = 0
        output = []

        for string in strs:
            sorted_str = str(sorted(string))
            if sorted_str in anagrams:
                output[anagrams[sorted_str]].append(string)
            else:
                output.append([string])
                anagrams[sorted_str] = current_sublist
                current_sublist += 1
        
        return output
            

            