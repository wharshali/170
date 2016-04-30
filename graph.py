import random
import os
import glob
import math
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

        self.vertices = []
        for i in range(self.size):
            f = i in ChildList
            self.vertices.append(Vertex(i, f))

        for column in range(self.size):
            for row in range(self.size):
                if self.matrix[column][row] == 1:
                    self.vertices[column].add_edge(self.vertices[row])

    def find_cycle(self, vertex):

        for neighbour in vertex.getNeighbors():
            if neighbour not in visited:
                if neighbour in path:
                    index = path.index(neighbour)
                    if (math.abs(index - len(path)) < 5):
                        return path[index:]
                else: 
                    path.append(neighbour)
                visited.add(neighbour)
                self.find_cycle(neighbour)
            path.remove(vertex)

    #V = vertex
    def remove_vertices(self, v):
        if v in self.vertices:
            v.neighbors = None
            for p in v.predeccesors:
                if p.neighbors:
                    p.neighbors.remove(v)

            self.vertices.remove(v)

    def solver(self):
        final_cycles = []
        num_nodes = len(self.vertices)
        counter = 0
        while counter < num_nodes/5:
            v = random.choice(self.vertices)
            cycle = self.find_cycle(v)
            if cycle == []:
                counter+=1
                break
            final_cycles.append(cycle)
            for v in cycle:
                self.remove_vertices(v)
        return final_cycles

    def solver_2(self):
        for vertex in self.vertices:
            path = [vertex]
            visited = set()
            cycle = self.find_cycle(vertex, path, visited)
            if cycle:
                return cycle
        return None

def main():
    adj = [[0 for x in range(20)] for y in range(20)]
    adj[0][1] = 1
    adj[1][2] = 1
    adj[2][1] = 1
    adj[2][3] = 1
    adj[3][4] = 1
    adj[4][2] = 1
    adj[5][6] = 1
    adj[6][7] = 1
    adj[7][8] = 1
    adj[8][9] = 1
    adj[9][5] = 1

    G = Graph(adj, [])
    cycle_list = G.solver_2()
    print "matt cycle is: ", cycle_list
    for v in cycle_list:
        print v.num

    # for i in range(1, 493):
    #     s = "phase1processed/" + str(i) + ".in"
    #     files.append(s)

    # for filename in files:
    #     f = open(filename, 'r')
    #     size = int(f.readline())
    #     children = list(map(int, f.readline().split()))
    #     matrix = [[0 for elm in range(size)] for elm in range(size)]
    #     row = f.readline()
    #     i = 0
    #     while (row and i < size):
    #         r = map(int, row.split())
    #         for j in range(size):
    #             matrix[j][i] = r[j]
    #         row = f.readline()
    #         i += 1
    #     largeList.append((size, children, matrix))

if __name__ == "__main__":
    main()
