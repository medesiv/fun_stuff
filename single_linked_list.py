# single linked list
'''
None

3 4 5
h   t
                                        
'''
import node.ListNode

class SingleLinkedList:
	def __init__(self, item, head=None):
		'''
		Initializes the list
		'''
		self.head = None
		self.tail = None

		return 

	def add(self, item):
		'''
		adds an item to the list
		'''
		if item is not instanceof(Node):
			item = ListNode(item)
		if self.head is None:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item

		return 

	def remove_by_id(self,id):
		'''
		removes an item from the list
		'''
		current_id = 1
		current_node = self.head
		previous_node = None
		while current_node is not None:
			if current_id == id:
				if previous_node is not None:
				previous_node.next = current_node.next
				else:
					self.head = current_node.next
					return

			previous_node = current_node
			current_node = current_node.next
			current_id = current_id + 1


	def size(self):
		'''size of the list'''
		count = 0

		curr_node = self.head
		while curr_node is not null:
			count+=1
			curr_node = curr_node.next
		return count


	def search(self,value):
		'''
		search for an item in the list
		'''
		current_node = self.head
		node_id = 1
		results = []
		while current_node is not None:
			if current_node.has_value(value):
				results.append(node_id)
			else:
				current_node = current_node.next
				node_id = node_id + 1

		return results

	def print_list(self):
		'''
		Prints the list
		'''
		current_node = self.head
		while current_node is not None:
			print(current_node.data)
			current_node = current_node.next

		return 
