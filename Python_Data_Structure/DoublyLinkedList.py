class Node:
	def __init__(self, data):
		self.data = data
		self.nref = None
		self.pref = None

class Dll:
	def __init__(self):
		self.head = None

	def print_dll(self):
		print()
		if self.head is None:
			print('(forward)List is empty')
		else:
			n = self.head
			while n is not None:
				print(n.data, '-->', end = " ")
				n = n.nref

	def print_dll_reverse(self):
		print()
		if self.head is None:
			print("(reverse)The list is empty")
		else:
			n = self.head
			while n.nref is not None:
				n = n.nref
				
			while n is not None:
				print(n.data, '-->', end=" ")
				n = n.pref
				

	def add_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.nref = self.head
			self.head.pref = new_node
			self.head = new_node

	def add_end(self, data):
		new_node = Node(data)
		
		if self.head is None:
			self.head = new_node
		else:
			n = self.head
			while n.nref is not None:
				n = n.nref
			n.nref = new_node
			new_node.pref = n
	def add_after(self, data, x):
		n = self.head
		while n is not None:
			if n.data == x:
				break
			n = n.nref
		if n is None:
			print("Given Node is not present in the list")
		elif n.nref is None:
			new_node = Node(data)
			n.nref = new_node
			new_node.pref = n 
		else:
			new_node = Node(data)
			n.nref.pref = new_node
			new_node.nref = n.nref
			n.nref = new_node
			new_node.pref = n
	
	def add_before(self, data, x):
		if self.head is None:
			print("linked list is empty")
		else:
			n = self.head
			while n is not None:
				if n.data == x:
					break
				n = n.nref
			if n is None:
				print("Given node does not exist")
			else:
				new_node = Node(data)
				new_node.nref = n
				new_node.pref = n.pref
				if n.pref is not None:
					n.pref.nref = new_node
				else:
					self.head = new_node
				n.pref = new_node

	def delete_begin(self):
		if self.head is None:
			print("List is empty")
		elif self.head.nref is None:
			self.head = None
			print("List is empty now")
		else:
			self.head = self.head.nref
			self.head.pref = None

	def delete_end(self):
		if self.head is None:
			print("List is empty")
		elif self.head.nref is None:
			self.head = None
			print("List is empty now")
		else:
			n = self.head
			while n.nref is not None:
				n = n.nref
			n.pref.nref = None

	def delete_by_value(self, x):
		if self.head is None:
			print('linked list is empty.')
			return
		if self.head.nref is None:
			if x == self.head.data:
				self.head = None
				print("list is empty now.")
			else:
				print(' value is not found in the list')
			return
		if self.head.data == x:
			self.head = self.head.nref
			self.head.pref = None
			return
		n = self.head
		while n.nref is not None:
			if x == n.data:
				break
			n = n.nref
		if n.nref is not None:
			n.pref.nref = n.nref
			n.nref.pref = n.pref
		else:
			if n.data == x:
				n.pref.nref = None
			else:
				print("Value is not found in the list")




dll = Dll()
dll.add_begin(60)
dll.add_end(151)
dll.add_begin(210)
dll.add_before(99,60)
dll.delete_by_value(210)
dll.print_dll()

dll.print_dll_reverse()






































