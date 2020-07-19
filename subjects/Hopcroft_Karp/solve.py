import math
import collections

def getRoots(aNeigh):
    def findRoot(aNode,aRoot):
        while aNode != aRoot[aNode][0]:
            aNode = aRoot[aNode][0]
        return (aNode,aRoot[aNode][1])
    myRoot = {}
    for myNode in aNeigh.keys():
        myRoot[myNode] = (myNode,0)
    for myI in aNeigh:
        for myJ in aNeigh[myI]:
            (myRoot_myI,myDepthMyI) = findRoot(myI,myRoot)
            (myRoot_myJ,myDepthMyJ) = findRoot(myJ,myRoot)
            if myRoot_myI != myRoot_myJ:
                myMin = myRoot_myI
                myMax = myRoot_myJ
                if  myDepthMyI > myDepthMyJ:
                    myMin = myRoot_myJ
                    myMax = myRoot_myI
                myRoot[myMax] = (myMax,max(myRoot[myMin][1]+1,myRoot[myMax][1]))
                myRoot[myMin] = (myRoot[myMax][0],-1)
    myToRet = {}
    for myI in aNeigh:
        if myRoot[myI][0] == myI:
            myToRet[myI] = []
    for myI in aNeigh:
        myToRet[findRoot(myI,myRoot)[0]].append(myI)
    return myToRet

def hopcroft():
    def bipartition(graph, root = 0, sub = None):
        u = [root]
        v = []
        treated = {k:False for k in sub} if sub is not None else {k:False for k in graph}

        select = False

        while not all(val == True for key, val in treated.items()):
            l = v if select else u
            k = u if select else v

            for vertice in l:
                if not treated[vertice]:
                    for connected in graph[vertice]:
                        if not treated[connected]:
                            k.append(connected)
                treated[vertice] = True

            select = not select
        return u, v

    def graph(edges):
        graph = {}
        for i in edges:
            if i[0] not in graph:
                graph[i[0]] = []
            if i[1] not in graph:
                graph[i[1]] = []
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        return graph

    def BFS (U, V, Pair_U, Pair_V, graph, Dist):
        queue = collections.deque()
        for u in U:
            if Pair_U[u] == -1:
                Dist[u] = 0
                queue.append(u)
        Dist[-1] = None
        while queue:
            u = queue.popleft()
            if Dist[-1] is None or Dist[u] < Dist[-1]:
                for v in graph[u]:
                    if Dist[ Pair_V[v] ] is None:
                        Dist[ Pair_V[v] ] = Dist[u] + 1
                        queue.append(Pair_V[v])
        return Dist[-1] is not None

    def DFS (u, Pair_U, Pair_V, graph, Dist):
        if u != -1:
            for v in graph[u]:
                if Dist[u] is not None and Dist[ Pair_V[v] ] and Dist[ Pair_V[v] ] == Dist[u] + 1:
                    if DFS(Pair_V[v], Pair_U, Pair_V, graph, Dist):
                        Pair_V[v] = u
                        Pair_U[u] = v
                        return True
            Dist[u] = None
            return False
        return True


    N = int(input())
    edges = []
    for i in range(N):
        (a, b) = input().split()
        edges.append((int(a), int(b)))
    graph = graph(edges)
    roots = getRoots(graph)
    U, V = [], []
    for i in roots:
        m, n = bipartition(graph, i, roots[i])
        U += m
        V += n
    graph[-1] = []


    Pair_U = {k:-1 for k in U}
    Pair_V = {k:-1 for k in V}
    Dist = {k:None for k in U}


    matching = 0
    while BFS(U, V, Pair_U, Pair_V, graph, Dist) :
        for u in U:
            if Pair_U[u] == -1:
                if DFS(u, Pair_U, Pair_V, graph, Dist) :
                    matching = matching + 1
    print(str(matching))

if __name__ == '__main__':
    hopcroft()
