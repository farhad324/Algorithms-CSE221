
def hamming_dist(str1, str2):
    
    count = 0
    char1=''
    char2=''
    
    
    if len(str1)>len(str2):
        x=len(str2)
    else:
        x=len(str1)
    i=0
    
    while(i < x):
        if(str1[i] != str2[i]):
            count += 1
            char1=char1+str1[i]
            char2=char2+str2[i]
        i += 1
          
    return count,char1,char2
 

str1 = "Moscow"
str2 = "Morocco"

print(hamming_dist(str1, str2))
 