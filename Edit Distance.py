def editDistance(str1, str2, m, n, ci=1,crm=1,crp=1):
    
    
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
 
    for i in range(m + 1):
        for j in range(n + 1):
 

            if i == 0:
                dp[i][j] = j    
 
            elif j == 0:
                dp[i][j] = i    
 
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                
            else:
                dp[i][j] = min((dp[i][j-1] + ci),             # Insert
                                   (dp[i-1][j] + crm),        # Remove
                                   (dp[i-1][j-1] + crp))      # Replace
                
         
    return dp[m][n] ##or dp[-1][-1]
 

str1 = "MARCH"
str2 = "CART"
cost_insert = 1
cost_remove = 1
cost_replace = 1
ed=editDistance(str1, str2, len(str1), len(str2), cost_insert,cost_remove,cost_replace)
print('Minimum Edit Distance:',ed)

## OUTPUT:
'''
Minimum Edit Distance: 3

'''