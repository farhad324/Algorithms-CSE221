def fracktionalKnapsack(weights,values,capacity):
    
    ratio = [v/w for v, w in zip(values, weights)]
    value_index_array=sorted(zip(ratio, weights),reverse=True)
    total = 0
    
    for i in value_index_array:       
        if i[1]<=capacity:
            capacity-=i[1]
            total+=i[0]*i[1]
        else:
            total+=i[0]*(capacity)
            break
        
    return total


item_weights = [10, 40, 20, 30]
item_values = [60, 40, 100, 120]
max_capacity = 50

total = fracktionalKnapsack(item_weights,item_values,max_capacity)

print('Maximum value we can obtain:',total)

##OUTPUT:
'''
Maximum value we can obtain: 240.0

'''