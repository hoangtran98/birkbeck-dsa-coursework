# Write a function AdjListInduced(G, S). The input of the function is a
# graph G in the form of adjacency lists and a subset of vertices of G stored
# in a list S. The function should return an adjacency lists presentation for
# the subgraph of G induced by S
def adjListInduced(G: list[list[int]], S: list[int]) -> list[list[int]]:
    n = len(G)

    # get the removed vertices from G to make S
    removed = []

    i = 0
    sIdx = 0

    while i < n and sIdx < len(S):

        if S[sIdx] != i:
            removed.append(i)
        else:
            sIdx += 1

        i += 1

    # Remove vertices from the graph
    output = G.copy()

    for vertex in removed:  # 0(logn)
        output[vertex] = []  # O(n)

        for o in output:  # O(n)
            if vertex in o:
                o.pop(o.index(vertex))  # O(n)

    return output


# Write a function IsConnected(G, S). The input of the function is a graph
# G in the form of adjacency lists and a subset of vertices of G stored in
# a list S. The function should return True if the subgraph of G induced
# by S is connected and False otherwise. Hint: combine the BFS with the
# function specified in the previous question.
def isConnected(G: list[list[int]], S: list[int]) -> bool:

    inducedS = adjListInduced(G, S)

    visited = [False] * len(G)
    BFSlist = []

    s = S[0]
    q = [s]
    visited[s] = True

    while q:
        curVertex = q.pop(0)
        BFSlist.append(curVertex)

        for vertex in inducedS[curVertex]:
            if not visited[vertex]:
                visited[vertex] = True
                q.append(vertex)

    if len(BFSlist) < len(S):
        return False
    else:
        return True
