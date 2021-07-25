class Node:
	"""
An object for storing a single node in a linked list

Attirbutes:
	data: data stored in node.
	next_node: reference to next node in linked list.
	"""

	def __init__(self, data, next_node = None):
		self.data = data
		self.ref = None


class LinkedList:
	def __init__(self):
		self.head = None

	def print_ll(self):
		if self.head is None:
			print("Linked List is empty.")
		else:
			n = self.head
			while n is not None:
				print(n.data, "-->", end=" ")
				n = n.ref

	def add_begin(self, data):
		new_node = Node(data)
		new_node.ref = self.head
		self.head = new_node

	def add_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			n = self.head
			while n.ref is not None:
				n = n.ref
			n.ref = new_node

	def add_after_node(self, data, x):
		n = self.head
		while n is not None:
			if x == n.data:
				break
			n = n.ref
		if n is None:
			print('node is not present in the list')
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def add_before_node(self, data, x):
		if self.head is None:
			print('Linked list is empty')
		if self.head.data == x:
			add_begin(data)
		n = self.head
		while n.ref is not None:
			if n.ref.data == x:
				break
			n = n.ref
		if n.ref is None:
			print("Node is not found!")
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def add_ifempty(self, data):
		if self.head is None:
			new_node = Node(data)
			self.head = new_node
		else:
			print('Linked List is not empty')
	def delete_begin(self):
		if self.head is None:
			print('The Linked List is empty')
		else:
			self.head = self.head.ref

	def delete_end(self):
		if self.head is None:
			print("Empty List")
		elif self.head.ref is None:
			self.head = None
		else:
			n = self.head
			while n.ref.ref is not None:
				n = n.ref
			n.ref = None

	def delete_node(self, x):
		if self.head is None:
			print("cannot delete ll, It is empty")
			return
		if x == self.head.data:
			self.head = self.head.ref
			return
		n = self.head
		while n.ref is not None:
			if n.ref.data == x:
				break
			n = n.ref
		if n.ref is None:
			print('Node is not found')
		else:
			n.ref = n.ref.ref



ll = LinkedList()
ll.add_begin(10)
ll.add_begin(100)
ll.add_begin(1000)
ll.add_begin(123456)
ll.delete_end()
ll.delete_node(200)
ll.print_ll()