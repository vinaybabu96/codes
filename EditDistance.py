class Solution:
    def help(self,word1,word2,i,j,dp):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in dp:
            if word1[i] == word2[j]:
                ans = self.help(word1, word2, i + 1, j + 1, dp)
            else: 
                insert = 1 + self.help(word1, word2, i, j + 1, dp)
                delete = 1 + self.help(word1, word2, i + 1, j, dp)
                replace = 1 + self.help(word1, word2, i + 1, j + 1, dp)
                ans = min(insert, delete, replace)
            dp[(i, j)] = ans
        return dp[(i, j)]
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)==0 and len(word2)==0 or word1==word2:
            return 0
        return self.help(word1,word2,0,0,{})