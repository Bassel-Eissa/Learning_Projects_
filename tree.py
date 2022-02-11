class BSTree:
	def __init__(self, key):
		self.key = key
		self.lchild = None
		self.rchild = None
	def insert(self, data):
		if self.key is None:
			self.key = data
			return
		if self.key == data:
			return
		if self.key > data:
			if self.lchild:
				self.lchild.insert(data)
			else:
				self.lchild = BSTree(data)
		else:
			if self.rchild:
				self.rchild.insert(data)
			else:
				self.rchild = BSTree(data)
	def search_node(self, data):
		if self.key == data:
			print("Node is found!")
			return
		if data < self.key:
			if self.lchild:
				if self.lchild.search_node(data):
					print(f"Node {data} is found in a leftchild of the tree")
				else:
					print(f"Node {data} is not present from lhcild")
				return
		else:
			if self.rchild:
				if self.rchild.search_node(data):
					print("Node is present in the right sub tree")
				else:
					print(f"Node {data} is not present from rchild")
				return

	def preorder(self):
		print(self.key, end=" ")
		if self.lchild:
			self.lchild.preorder()
		if self.rchild:
			self.rchild.preorder()
	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key, end=" ")
		if self.rchild:
			self.rchild.inorder()
	def postorder(self):
		if self.lchild:
			self.lchild.postorder()
		if self.rchild:
			self.rchild.postorder()
		print(self.key, end=" ")

	def delete(self, data, curr):
		#Check if the tree is empty
		if self.key is None:
			print("Tree is empty")
			return

		#Find the position of the node to delete
		if data < self.key:
			if self.lchild:
				self.lchild = self.lchild.delete(data, curr)  
			else:
				print("Given node is not present in the tree")
		elif data > self.key:
			if self.rchild:
				self.rchild = self.rchild.delete(data, curr)
			else:
				print("Given node is not present in Rtree")
		else:
			#Checking the children of the node we want to delete
			if self.lchild is None:
				temp = self.rchild
				if data == curr:
					self.key = temp.key
					self.lchild = temp.lchild
					self.rchild = temp.rchild
					temp = None
					return
				self = None
				return temp
			if self.rchild is None:
				temp = self.lchild
				if data == curr:
					self.key = temp.key
					self.lchild = temp.lchild
					self.rchild = temp.rchild
					temp = None
				return temp
			node = self.rchild
			while self.lchild:
				node = self.lchild
			self.key = node.key
			self.rchild = self.rchild.delete(node.key)
		return self

	def count(node):
		if node is None:
			return 0
		return 1+ count(node.lchild) + count(node.rchild)

	def getMin(self):
		current = self
		while current.lchild:
			current = current.lchild
		print(f"The smallest node in the tree is {current.key}")

	def getMax(self):
		current = self
		while current.rchild:
			current = current.rchild
		print(f"The greatest node in the tree is {current.key}")



root = BSTree(10)
list1 = [20, 4, 30, 100, 5]
for i in list1:
	root.insert(i)

root.search_node(20)
root.delete(20, root.key)
print("Preorder")
print(root.preorder())
print("Inorder")
print(root.inorder())
print("PostOrder")
print(root.postorder())
root.getMax()













		