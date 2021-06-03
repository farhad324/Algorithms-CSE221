def RLE(string):
    
    encoded=''
    i = 0
    
    while i < len(string)- 1:
        count = 1
        
        while (i < len(string) - 1 and string[i] == string[i + 1]):
            count += 1
            i += 1
        i += 1
 
        encoded+= string[i - 1] +str(count)
        
    return encoded
 
string = "ww22222wwwwwaaaadexpppxxxxxywww"
x=RLE(string)
print('Encoded String:',x)

##OUTPUT:
'''

Encoded String: w4a3d1e1x6y1w3
'''