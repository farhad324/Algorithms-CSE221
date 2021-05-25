import math
 
def minimax (current, node_index,turn, scores,targetDepth):
 
    if (current == targetDepth):
        return scores[node_index]
     
    if (turn):

        return max(minimax(current + 1, node_index * 2,False, scores, targetDepth),
                   minimax(current + 1, node_index * 2 + 1,False, scores, targetDepth))
     
    else:
        return min(minimax(current + 1, node_index * 2,True, scores, targetDepth),
                   minimax(current + 1, node_index * 2 + 1,True, scores, targetDepth))
     
scores = [-1,3,5,1,-6,-4,0,9]
 
treeDepth = math.log(len(scores), 2)



result = minimax(0, 0, True, scores, treeDepth)

print("The optimal value is:",result, end = "")

'''
The optimal value is: 3

'''