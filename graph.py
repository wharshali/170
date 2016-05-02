import random
import os
import glob
import unittest
import time

largeList = []
files = []

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
        self.matrix = adjacency_matrix
        self.size = len(adjacency_matrix)
        self.penalty = self.size + len(self.children)
        self.vertices = []
        for i in range(self.size):
            f = i in ChildList
            self.vertices.append(Vertex(i, f))

        for column in range(self.size):
            for row in range(self.size):
                if self.matrix[column][row] == 1:
                    self.vertices[column].add_edge(self.vertices[row])

    def get_penalty(self):
        return self.penalty

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

    def remove_vertices(self, v):
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

class GraphUnitTests(unittest.TestCase):
    def test_DiffCycles(self):
        a = [[0 for x in range(7)] for y in range(7)]
        a[0] = [0,1,0,0,0,0,1]
        a[1] = [1,0,0,1,0,0,0]
        a[2] = [0,0,0,1,0,0,0]
        a[3] = [0,1,0,0,1,0,0]
        a[4] = [1,0,0,0,0,0,0]
        a[5] = [1,0,0,0,0,0,0]
        a[6] = [0,0,0,0,1,1,0]
        graphCycles = []
        for i in range(5):
            G = Graph(a, [])
            cycle_list = []
            cycles = G.solver()
            for c in cycles:
                l = []
                for v in c:
                    l.append(v.num)
                cycle_list.append(l)
            graphCycles.append((cycle_list, G.get_penalty()))
        bestCycles = min(graphCycles, key=lambda x : x[1])[0]
        print(bestCycles)


    


def main():

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

    with open("solutions.out", 'w+') as f:
        for size, childList, adj in largeList:
            graphCycles = []
            for i in range(5):
                G = Graph(adj, childList)
                cycle_list = []
                cycles = G.solver()
                for c in cycles:
                    l = []
                    for v in c:
                        l.append(v.num)
                    cycle_list.append(l)
                graphCycles.append((cycle_list, G.get_penalty()))
            bestCycles = min(graphCycles, key=lambda x : x[1])[0]
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
    main()
