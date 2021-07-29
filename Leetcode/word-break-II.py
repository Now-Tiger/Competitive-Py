'''
problem : Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
          Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
 
Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

Explanation: Note that you are allowed to reuse a dictionary word.
'''

def wordbreak(s:str, worddict:list[str]) -> list[str] :
    m = set(worddict)

    @lru_cache(None)

    def dfs(idx) :
        if idx >= len(s) :
            return [""] 
        
        res = []
        for i in range(idx + 1, len(s) + 1) :
            curr = s[idx:i]
            if curr in m :
                val = dfs[i]
                for each in val :
                    res.append(curr + " " + each if len(each) != 0 else curr)
        return res
    return dfs[0] 