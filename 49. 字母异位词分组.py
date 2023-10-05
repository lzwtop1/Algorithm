class Solution:
    def groupAnagrams(self, strs):
        d={}
        for iterm in strs:
            d_key=tuple(sorted(iterm))
            d[d_key]=d.get(d_key,[])+[iterm]
        return list(d.values())

# 示例输入
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result=Solution()
print(result.groupAnagrams(strs))