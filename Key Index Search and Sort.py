class KeyIndex:
    def __init__(self,a):
        self.a=a
        self.aux=[0]*(max(a)+1)
        for i in self.a:
            self.aux[i]+=1
            
    def search(self,item):
        if self.aux[item]!=0:
            return True
        else:
            return False
        
    def sort(self):
        sorted_a=[]
        for i in range(len(self.aux)):
            if self.aux[i]!=0:
                sorted_a+=[i]*self.aux[i]
        return sorted_a
    def sort_neg(self,a):
        neg_min=min(a)
        x=neg_min*-1
        for i in range(len(a)):
            a[i]+=x
        aux2=[0]*(max(a)+1)
        for i in a:
            aux2[i]+=1
        
        sorted_neg_a=[]
        for i in range(len(aux2)):
            if aux2[i]!=0:
                sorted_neg_a+=[i]*aux2[i]
        
        for i in range(len(sorted_neg_a)):
            sorted_neg_a[i]+=neg_min
            
        return sorted_neg_a
    
key_ind=KeyIndex([4,2,3,4,7,4])
print('Is 3 in the array:',key_ind.search(3))
print('Sorted Array:',key_ind.sort())
print('Sorted Array with Negative Numbers:',key_ind.sort_neg([4,-2,3,-4,7,4]))
##OUPUT:
'''
Is 3 in the array: True
Sorted Array: [2, 3, 4, 4, 4, 7]

'''
