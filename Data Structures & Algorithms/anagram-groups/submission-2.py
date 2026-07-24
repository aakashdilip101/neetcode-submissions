class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for string in strs:
            sorted_str = tuple(sorted(string))
            if not sorted_str in hm:
                hm[sorted_str] = []

            hm[sorted_str].append(string)
        
        return list(hm.values())