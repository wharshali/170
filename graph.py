import random
import os
import glob
import unittest
import time
import pdb

largeList = []
files = []

"""returns the data from *.in files as a list of adjacency matricies"""
def fetchData():
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
                if (r[j] == 1):
                    matrix[i][j] = 1
            row = f.readline()
            i += 1
        largeList.append((size, children, matrix))

"""Same as above but used for testing"""
def fetchDataTesting():
    f = open("testinput/test1.in", 'r')
    size = int(f.readline())
    children = list(map(int, f.readline().split()))
    matrix = [[0 for elm in range(size)] for elm in range(size)]
    row = f.readline()
    i = 0
    while (row and i < size):
        r = map(int, row.split())
        for j in range(size):
            if (r[j] == 1):
                matrix[i][j] = 1
        row = f.readline()
        i += 1
    return (size, children, matrix)

"""Input: One valid list of the cycles and the Graph that the list belongs to."""
def validateCycles(G, cycleList):
    error_edges = []
    matrix = G.get_Matrix()
    for cycle in cycleList:
        for i in range(len(cycle)-1):
            if not (matrix[cycle[i]][cycle[i+1]]):
                error_edges.append((cycle[i],cycle[i+1]))
        if not (matrix[cycle[-1]][cycle[0]]):
            error_edges.append((cycle[-1],cycle[0]))
    return error_edges

class Vertex:
    def __init__(self, num, isChild):
        self.edges = []
        self.neighbors = []
        self.child = isChild
        self.num = num
        self.predeccesors = []

    def edges(self):
        return self.edges

    def add_edge(self, v):
        self.edges.append(Edge(v, self))
        self.neighbors.append(v)
        v.predeccesors.append(self)

    def getNeighbors(self):
        return self.neighbors

    def isChild(self):
        return self.child

    def __str__(self):
        return self.num

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
        self.remaining_children = []
        self.matrix = adjacency_matrix
        self.size = len(adjacency_matrix)
        self.penalty = self.size + len(self.children)
        self.vertices = []
        for i in range(self.size):
            f = i in ChildList
            self.vertices.append(Vertex(i, f))
            if f:
                self.remaining_children.append(Vertex(i,f))

        for column in range(self.size):
            for row in range(self.size):
                if self.matrix[column][row] == 1:
                    self.vertices[column].add_edge(self.vertices[row])

    def get_penalty(self):
        return self.penalty

    def get_Matrix(self):
        return self.matrix

    def getRandNode(self):
        select_lst = self.vertices + self.remaining_children
        if len(select_lst) > 0:
            return random.choice(select_lst)
        return None

    def find_cycle(self, vertex):

        def find_cycle_to_ancestor(node, ancestor):
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
            # Recursively explore the connected component
            for neighbour in node.neighbors:
                if (cycle):
                    return
                if (neighbour not in visited):
                    spanning_tree[neighbour] = node
                    dfs(neighbour)
                else:
                    if (spanning_tree[node] != neighbour):
                        cycle.extend(find_cycle_to_ancestor(node, neighbour))
                        

        visited = {}              # List for marking visited and non-visited nodes
        spanning_tree = {}        # Spanning tree
        cycle = []

        # Select a non-visited node
        spanning_tree[vertex] = None 
        dfs(vertex)
        if (cycle) and len(cycle) <= 5:
            return cycle
        return []

    def remove_vertices(self, v):
        if v in self.children:
            self.remaining_children.remove(v)
        if v in self.vertices:
            v.neighbors = None
            for p in v.predeccesors:
                if p.neighbors:
                    p.neighbors.remove(v)
            if v.num in self.children:
                self.penalty -= 2
            else:
                self.penalty -= 1
            self.vertices.remove(v)

    def solverRand(self):
        final_cycles = []
        num_nodes = len(self.vertices)
        counter = 0
        while counter < num_nodes/5:
            if not self.vertices == []:
                v = self.getRandNode()
                cycle = self.find_cycle(v)
                if cycle == [] or len(cycle) > 5:
                    counter+=1
                else:
                    final_cycles.append(cycle)
                    for v in cycle:
                        self.remove_vertices(v)
            else:
                break
        return final_cycles

    def solver(self):
        final_cycles = []
        num_nodes = len(self.vertices)
        counter = 0
        while counter < num_nodes/5:
            if not self.vertices == []:
                v = random.choice(self.vertices)
                cycle = self.find_cycle(v)
                if cycle == [] or len(cycle) > 5:
                    counter+=1
                else:
                    final_cycles.append(cycle)
                    for v in cycle:
                        self.remove_vertices(v)
            else:
                break
        return final_cycles


    def 

class GraphUnitTests(unittest.TestCase):
    def test_DiffCycles(self):
        a = [[0 for x in range(7)] for y in range(7)]
        a[1][0] = 1
        a[6][0] = 1
        a[0][1] = 1
        a[3][1] = 1
        a[3][2] = 1
        a[1][3] = 1
        a[4][3] = 1
        a[0][4] = 1
        a[0][5] = 1
        a[5][6] = 1
        a[4][6] = 1
        graphCycles = []
        for i in range(5):
            G = Graph(a, [])
            cycle_list = []
            cycles = G.solverRand()
            for c in cycles:
                l = []
                for v in c:
                    l.append(v.num)
                cycle_list.append(l)
            graphCycles.append((cycle_list, G.get_penalty()))
        bestCycles = min(graphCycles, key=lambda x : x[1])[0]
        checkSet = validateCycles(G, bestCycles)
        self.assertEquals(len(checkSet), 0)

def main():
    """Getting input Data"""
    fetchData()
    
    """Solving for cycles and selecting the lowest penatly"""
    with open("solutions.out", 'w+') as f:
        for size, childList, adj in largeList:
            graphCycles = []

            """Run 5 times picking random vertex"""
            for i in range(5):
                G = Graph(adj, childList)
                cycles = G.solver()
                cycle_list = [[vertex.num for vertex in cycle] for cycle in cycles]
                graphCycles.append((cycle_list, G.get_penalty()))

            """Run 5 times with weighted random choice"""
            for i in range(5):
                G = Graph(adj, childList)
                cycles = G.solverRand()
                cycle_list = [[vertex.num for vertex in cycle] for cycle in cycles]
                graphCycles.append((cycle_list, G.get_penalty()))
                
            bestCycles = min(graphCycles, key=lambda x : x[1])[0]
            print([elm[1] for elm in graphCycles])
            
            """Validating found Cycles"""
            for cycles in graphCycles:
                errors = validateCycles(G, cycles[0])
                if (errors != []):
                    print([elm for elm in errors])
                    print(G.get_Matrix())

            """Writing to file"""
            if bestCycles == []:
                f.write("None\n")
            else:
                for i, cycle in enumerate(bestCycles):
                    if i == len(bestCycles) - 1:
                        f.write(" ".join(str(x) for x in cycle))
                    else:
                        f.write(" ".join(str(x) for x in cycle) + "; ")
                f.write("\n")


if __name__ == "__main__":
    #unittest.main()
    main()