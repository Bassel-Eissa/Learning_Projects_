#Add node using dict method...
def add_node_map(v):
	if v in graph:
		print("Node is already present in the graph")
	else:
		graph[v] = []


def add_edge_map(v1, v2, cost):
	if v1 not in graph:
		print(f"{v1} is not present in the graph")
	elif v2 not in graph:
		print(f"{v1} is not present in the graph")
	else:
		graph[v1].append([v2, cost])
		#Incase of a directed graph so we will comment the line below and direction will be 
		#from v1 to v2
		graph[v2].append([v1, cost])

#Delete for directed unweighted graph 
def delete_node(v):
	if v not in graph:
		print("Node is not present in the graph")
	else:
		graph.pop(v)
		for i in graph:
			list1 = graph[i]
			if v in list1:
				list1.remove(v)


#Delete for weighted graphs
def delete_node(v):
	if v not in graph:
		print("Node is not present in the graph")
	else:
		graph.pop(v)
		for i in graph:
			list1 = graph[i]
			for item in list1:
				if v == item[0]:
					list1.remove(item)
					break


def delete_edge(v1, v2):
	if v1 not in graph:
		print("There is no edge to remove.")
	elif v2 not in graph:
		print("There is no edge to remove.")
	else:
		if len(graph[v1]) > 1:
			for i in graph[v1]:
				if v2 in i:
					i.clear()
			for i in graph[v2]:
				if v1 in i:
					i.clear()
		else:
			if v2 in graph[v1]:
				graph[v1].remove(v2)
				graph[v2].remove(v1)
			else:
				print("There is no edge between these two nodes.")



graph = {}
node_count = 0

print("Before adding nodes")
print(graph)
add_node_map("A")
add_node_map("B")
add_node_map("C")
add_edge_map("A", "B", 2)
add_edge_map("A", "C", 3)
add_edge_map("C", "B", 4)
delete_edge("A", "B")
print("After adding nodes")
print(graph)

























