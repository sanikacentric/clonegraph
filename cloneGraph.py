class Node :
    def __init__(self, val=0,neighbours=0):
        self.val = val
        self.neighbours= neighbours if not None else []

class Solution :
    def cloneGraph (self, node :[Node])->Node:
        oldToNew ={}

        def dfs (node):
            if node in oldToNew :
                return oldToNew[node]  

            copy = oldToNew[node]

            oldToNew[Node]=copy 

            for nei in node.neighbours :
                copy.neighbours.append(dfs(nei))
            return copy

        return dfs(node) if  node else None      

