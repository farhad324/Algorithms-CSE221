class LCS:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
        self.m=len(str1)
        self.n=len(str2)
        self.dp = [[0 for x in range(self.n + 1)] for x in range(self.m + 1)]

    def lcs_length(self):
        for i in range(self.m): 
            for j in range(self.n):
                if self.str1[i] == self.str2[j]:
                    self.dp[i+1][j+1]=self.dp[i][j]+1
                else:
                    self.dp[i+1][j+1]=max(self.dp[i][j+1],self.dp[i+1][j])
                    
        return self.dp[-1][-1]
    
    def lcs_sequence(self):
        index = self.dp[self.m][self.n]
        seq = [""] * (index+1)
        seq[index] = ""
        i,j = self.m,self.n 
        while i > 0 and j > 0:
            if self.str1[i-1] == self.str2[j-1]:
                seq[index-1] = self.str1[i-1]
                i = i - 1
                j = j - 1
                index -= 1
            elif self.dp[i][j-1] < self.dp[i-1][j]:
                i = i - 1
            else:
                j = j - 1
        seq_str=''.join(seq[:-1])
        return seq_str


str1 = "CDEFGABC"
str2 = "CEFDABGAC"
MySeq=LCS(str1,str2)
print('Least Common Subsequence length-->',MySeq.lcs_length())
print('Least Common Subsequence-->',MySeq.lcs_sequence())


##OUTPUT:
'''
Least Common Subsequence length--> 6
Least Common Subsequence--> CEFABC

'''
