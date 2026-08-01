from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for i in strs:
            s=sorted(i)
            key="".join(s)
            group[key].append(i)
        op=list(group.values())
        return op

        