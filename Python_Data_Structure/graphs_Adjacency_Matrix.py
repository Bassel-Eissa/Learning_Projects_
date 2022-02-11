def add_node(v):
	global node_count
	if v in nodes:
		print("The node is already present in the graph")
	else:
		node_count += 1
		nodes.append(v)
		for n in graph:
			n.append(0)
		temp = []
		for i in range(node_count):
			temp.append(0)
		graph.append(temp)

def add_edge(v1, v2, cost):
	if v1 not in nodes:
		print(f"{v1} is not present in the graph")
	elif v2 not in nodes:
			print(f"{v2} is not present in the graph")
	else:
		index_1 = nodes.index(v1)
		index_2 = nodes.index(v2)
		graph[index_1][index_2] = cost
		graph[index_2][index_1] = cost


def print_graph():

	for i in range(node_count):
		for j in range(node_count):
			print(graph[i][j], end = " ")
		print()

def delete_node(v):
	global node_count
	if v not in nodes:
		print(f"Node {v} is not present in the graph")
	else:
		index1 = nodes.index(v)
		node_count -= 1
		nodes.remove(v)
		graph.pop(index1)
		for i in graph:
			i.pop(index1)

#for single edges only...
def delete_edge(v1, v2):
	if v1 not in nodes:
		print(f"{v1} is not present in the graph")
	elif v2 not in nodes:
		print(f"{v2} is not present in the graph")
	else: 
		#If we are working on a directed graph
		#Comment any of the last two lines of code in this func
		#According the the direction of the graph
		index1 = nodes.index(v1)
		index2 = nodes.index(v2)
		graph[index1][index2] = 0
		graph[index2][index1] = 0




nodes = []
graph = []
node_count = 0

print("Before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 2)
add_edge("A", "C", 3)
add_edge("C", "B", 4)

print("After adding nodes")
delete_edge("A", "C")
print(nodes)
print(graph)
delete_node('B')
print_graph()

























