import collections
from collections import defaultdict

def groupAnagrams(self, strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()
print(groupAnagrams(groupAnagrams,["eat","tea","tan","ate","nat","bat"]))