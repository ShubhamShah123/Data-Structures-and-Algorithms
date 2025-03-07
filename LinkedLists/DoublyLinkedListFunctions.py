from Node import DLLNode as dNode
from Stack import Stack

def convertArr2DLL(array: list) -> dNode:
	head = dNode(array[0])
	N = len(array)
	prev = head
	for i in range(1,N):
		tempNode = dNode(array[i], None, prev)
		prev.next = tempNode
		prev = prev.next
	return head

def traverseDLL(head: dNode):
	output = []
	while head:
		output.append(str(head.data))
		head = head.next
	return output

def deleteHead(head: dNode) -> dNode:
	if not head: return None
	if head.next is None and head.back is None: return None
	prev = head
	head = head.next
	head.back = None
	prev.next = None
	return head

def deleteTail(head: dNode) -> dNode:
	if not head: return None
	if head.next is None and head.back is None: return None
	temp = head
	while temp.next:
		temp = temp.next
	prev = temp.back
	prev.next = None
	temp.back = None
	return head

def deleteAtK(head: dNode, k: int) -> dNode:
	if not head or not head.next: return None
	temp = head
	cnt = 0
	while temp:
		cnt += 1
		if cnt == k:
			break
		temp = temp.next
	prev = temp.back
	front = temp.next
	if prev is None and front is None:
		return None
	elif prev is None:
		return deleteHead(head)
	elif front is None:
		return deleteTail(head)
	prev.next = front
	front.back = prev
	temp.next = None
	temp.back = None
	return head

def deleteValue(head: dNode, value: int) -> dNode:
	if head.data == value: return head
	temp = head
	while temp:
		if temp.data != value:
			temp = temp.next
		else:
			break

	prev = temp.back
	front = temp.next
	if not front:
		prev.next = None
		temp.back = None
		return head
	
	prev.next = front
	front.back = prev

	temp.next = None
	temp.back = None
	return head

def insertBeforeHead(head: dNode, value: int) -> dNode:
	if not head: return dNode(value)
	newNode = dNode(value, head, None)
	head.back = newNode
	return newNode

def insertBeforeTail(head: dNode, value: int) -> dNode:
	if not head: return dNode(value)
	temp = head
	while temp.next:
		temp = temp.next
	prev = temp.back
	newNode = dNode(value, temp, prev)
	prev.next = newNode
	temp.back = newNode
	return head

def insertBeforeK(head: dNode, k: int, value: int) -> dNode:
	if k == 1: return insertBeforeHead(head, value)
	temp = head
	cnt = 0
	while temp:
		cnt += 1
		if cnt == k: break
		temp = temp.next
	prev = temp.back
	newNode = dNode(value, temp, prev)
	prev.next = newNode
	temp.back = newNode
	return head

def insertBeforeValue(head: dNode, el: int, value: int) -> dNode:
	if head.data == el: return insertBeforeHead(head, value)
	temp = head
	while temp:
		if temp.data == el:
			break
		else:
			temp = temp.next
	prev = temp.back
	newNode = dNode(value, temp, prev)
	prev.next = newNode
	temp.back = newNode
	return head
	
def insertAfterHead(head: dNode, value: int) -> dNode:
	temp = head
	newNode = dNode(value, head.next, head)
	head.next = newNode
	newNode.next.back = newNode
	return head

def insertAfterTail(head: dNode, value: int) -> dNode:
	temp = head
	while temp.next:
		temp = temp.next
	newNode = dNode(value, None, temp)
	temp.next = newNode
	return head

def insertAfterK(head: dNode, value: int, k: int) -> dNode:
	temp = head
	cnt = 0
	while temp:
		cnt += 1
		if cnt == k:
			break
		temp = temp.next
	newNode = dNode(value, temp.next, temp)
	temp.next = newNode
	newNode.next.back = newNode
	return head

def insertAfterValue(head: dNode, value: int, el: int) -> dNode:
	temp = head
	while temp:
		if temp.data == el:
			break
		temp = temp.next
	newNode = dNode(value, temp.next, temp)
	temp.next = newNode
	newNode.next.back = newNode
	return head

def reverseUsingStack(head: dNode) -> dNode:
	st = Stack()
	# Step 1: Pushing to Stack
	temp = head
	while temp:
		st.push(temp.data)
		temp = temp.next

	# Step 2: Popping from stack
	temp = head
	while temp:
		temp.data = st.pop()
		temp = temp.next
	return head

def reverseOnePass(head: dNode) -> dNode:
	if not head or not head.next: return head
	curr = head
	prev = None
	while curr:
		prev = curr.back
		curr.back = curr.next
		curr.next = prev
		curr = curr.back
	return prev.back

def deleteAllOccurence(head: dNode, key: int) -> dNode:
	print(f">> Input list: {' <-> '.join(traverseDLL(head))}\n>> Key: {key}")
	temp = head
	while temp:
		if temp.data == key:
			if temp == head:
				head = head.next
			nextNode = temp.next
			prevNode = temp.back
			if nextNode: nextNode.back = prevNode
			if prevNode: prevNode.next = nextNode
			temp = nextNode
		else:
			temp = temp.next
	return head

def getParisWithSum_v1(head: dNode, sum: int) -> list:
	temp1 = head
	output = []
	while temp1:
		temp2 = temp1.next
		while temp2 and temp1.data + temp2.data <= sum:
			if temp1.data + temp2.data == sum:
				output.append([temp1.data, temp2.data])
			temp2 = temp2.next
		temp1 = temp1.next
	return output

def getParisWithSum_v2(head: dNode, sum: int) -> list:
	left, right = head, head
	output = []
	while right.next:
		right = right.next

	while left.data < right.data:
		tempSum = left.data + right.data
		if tempSum == sum:
			output.append([left.data, right.data])
			left = left.next
			right = right.back
		elif tempSum < sum:
			left = left.next
		else:
			right = right.back
	return output

def removeDuplicates(head: dNode) -> dNode:
	if not head or not head.next: return head
	print(f">> Input List: {' <-> '.join(traverseDLL(head))}")
	temp = head
	while temp and temp.next:
		nextNode = temp.next
		while nextNode and nextNode.data == temp.data:
			nextNode = nextNode.next
		temp.next = nextNode
		if nextNode: nextNode.back = temp
		temp = temp.next
	return head
	