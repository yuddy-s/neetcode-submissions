class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        result = []

        for item in strs:
            string = ''.join(sorted(item))
            if string not in groups:
                groups.append(string)
                result.append([item])
            else:
                i = groups.index(string)
                result[i].append(item)


        return result
            