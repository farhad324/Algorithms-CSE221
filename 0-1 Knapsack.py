def knapsack(n, c, w, v):

    K = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(c + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif w[i-1] <= j:
                K[i][j] = max(v[i-1] + K[i-1][j-w[i-1]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
  
    
    return K

def show(n, c, w, value, items):
    
    j = c
    selected=[]
    for i in range(n,0,-1):
        if value[i][j] > value[i-1][j]:
            selected.insert(0,items[i-1])
            j -= w[i - 1]
            
    print('Items Taken:')
    print(*selected,sep=', ')
    print('Total amount taken:', value[n][c])


values=[60, 100, 120 ]
weights=[10, 20, 30]
item_names=['Spice','Sugar','Rice']


max_weight=50
no_of_items=3


k=knapsack(no_of_items,max_weight,weights,values)
show(no_of_items,max_weight,weights,k,item_names)

##OUTPUT:
'''
Items Taken:
Sugar, Rice
Total amount taken: 220

'''