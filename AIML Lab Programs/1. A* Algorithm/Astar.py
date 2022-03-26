def aStar(startNode, stopNode):
    openSet = set(startNode)
    closedSet = set()
    g = {}
    parents = {}
    g[startNode] = 0
    parents[startNode]=startNode

    while len(openSet)>0:
        n = None
        for v in openSet:
            if n == None or g[v]+heuristic(v) > g[n]+heuristic(n):
                n = v
        if n == stopNode or graphNode[n]== None:
            pass
        else:
            for (m, weight) in getNeighbour(n):
                if m not in openSet and m not in closedSet:
                    openSet.add(m)
                    parents[m] = n
                    g[m] = g[n]+ weight
                else:
                    if g[m] > g[n]+ weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closedSet:
                            closedSet.remove(m)
                            openSet.add(m)
        if n ==None:
            print("Path Doesnot Exist")
            return None

        if n==stopNode:
            path=[]
            while parents[m] != n:
                path.append(n)
                n= parents[n] 
            path.append(startNode)
            path.reverse
            print("path found: {}".format(path))
            return path
        openSet.remove(n)
        closedSet.add(n)
    print("Path doesnot exist")
    return None
def getNeighbour(v):
    if v in graphNode:
        return graphNode[v]
    else:
        return None
        
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]
graphNode = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
 }
                    
aStar('A', 'J')


