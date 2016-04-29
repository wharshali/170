import pygraph
from pygraph.algorithms import cycles
from pygraph.algorithms import searching
from pygraph.classes import digraph




def build_kidney_graph(nodes, edges):
	"""
	nodes: List of nodes: [0,1,2,3,4,5]
	edges: Tuples of edges from node to node: [(0,1),(2,3)]
	"""

	gr = digraph.digraph()
	gr.add_nodes(nodes) # May not work from reading doc
	for edge in edges:
		gr.add_edge(edge)

	return gr




def main():
	nodes = [0,1,2,3,4,5,6,7,8]
	edges = [(0,1), (2,3), (3, 4), (4, 2)]
	gr = build_kidney_graph(nodes, edges)
	#print gr.nodes()

	cycs = cycles.find_cycle(gr)
	print "cycle is: ", cycs




if __name__ == "__main__":
	main()

