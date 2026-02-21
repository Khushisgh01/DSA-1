from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            words[key].append(word)
        
        return list(words.values())
