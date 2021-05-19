def editDistance(str1, str2, m, n,ci=1,crm=1,crp=1):
 
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1,ci,crm,crp)
 
    return min( editDistance(str1, str2, m, n-1,ci,crm,crp)+ci,       # Insert
                editDistance(str1, str2, m-1, n,ci,crm,crp)+crm,      # Remove
                editDistance(str1, str2, m-1, n-1,ci,crm,crp)+crp )   # Replace

 

str1 = "tea"
str2 = "set"
ed=editDistance(str1, str2, len(str1), len(str2))
print ('Minimum Edit Distance:',ed)
 
## OUTPUT:
'''
Minimum Edit Distance: 2
'''