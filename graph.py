import random
import os
import glob
largeList = []
files = []
for i in range(1, 493):
    s = "phase1processed/" + str(i) + ".in"
    files.append(s)

for filename in files:
    f = open(filename, 'r')
    size = int(f.readline())
    children = list(map(int, f.readline().split()))
    matrix = [[0 for elm in range(size)] for elm in range(size)]
    row = f.readline()
    i = 0
    while (row and i < size):
        r = map(int, row.split())
        for j in range(size):
            matrix[j][i] = r[j]
        row = f.readline()
        i += 1
    largeList.append((size, children, matrix))

class Vertex:
    def __init__(self, num, isChild):
        self.edges = []
        self.neighbors = []
        self.child = isChild
        self.num = num

    def edges(self):
        return self.edges

    def add_edge(self, v):
        self.edges.append(Edge(v, self))
        self.neighbors.append(v)

    def neighbors(self):
        return self.neighbors

    def isChild(self):
        return self.child

class Edge:
        def __init__(self, head, tail):
            self.head = head
            self.tail = tail

        def tail(self):
            return self.tail 

        def head(self):
            return self.head

class Graph:

    #MATRIX IS READ FROM FILE AS A 2D ARRAY
    def __init__(self, adjacency_matrix, ChildList):
        self.children = ChildList
        self.matrix = adjacency_matrix
        self.size = len(adjacency_matrix)

        self.vertices = []
        for i in range(self.size):
            f = i in ChildList
            self.vertices.append(Vertex(i, f))

        for column in range(self.size):
            for row in range(self.size):
                if self.matrix[column][row] == 1:
                    self.vertices[column].add_edge(self.vertices[row])


    def find_cycle(self, vertex):

        def find_cycle_to_ancestor(node, ancestor):
            """
            Find a cycle containing both node and ancestor.
            """
            path = []
            while (node != ancestor):
                if (node is None):
                    return []
                path.append(node)
                node = spanning_tree[node]
            path.append(node)
            path.reverse()
            return path
        
        def dfs(node):
            visited[node] = 1
            # Explore recursively the connected component
            for each in node.neighbors:
                if (cycle):
                    return
                if (each not in visited):
                    spanning_tree[each] = node
                    dfs(each)
                else:
                    if (spanning_tree[node] != each):
                        cycle.extend(find_cycle_to_ancestor(node, each))


        visited = {}              # List for marking visited and non-visited nodes
        spanning_tree = {}        # Spanning tree
        cycle = []

        # Select a non-visited node
        spanning_tree[vertex] = None 
        dfs(vertex)
        if (cycle) and len(cycle) <= 5:
            return cycle
        return []

    #V is a vertex object
    def get_out_edges(self, v):
        if (elf.vertices[v] == None):
            return []
        return self.vertices[v].edges()


    #VERTICES is a list of vertices (indices)
    def remove_vertices(v):
        self.vertices[v] = None


def main():
    adj = [[0 for x in range(5)] for y in range(5)]
    adj[0][1] = 1
    adj[2][3] = 1
    adj[3][4] = 1
    adj[4][2] = 1

    G = Graph(adj, [])
    #print gr.nodes()
    node = random.choice(G.vertices)
    cycs = G.find_cycle(node)
    cycle = []
    for v in cycs:
        cycle.append(v.num)
    print "cycle is: ", cycle


if __name__ == "__main__":
    main()
