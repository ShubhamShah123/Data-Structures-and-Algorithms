from Node import Node, ChildListNode, RandomNode
from Stack import Stack
from heapq import heappush, heappop, heapify

def convertArr2LL(array: list) -> Node:
	if not array: return Node(None)
	head = Node(array[0])
	mover = head
	for i in range(1, len(array)):
		temp = Node(array[i])
		mover.next = temp
		mover = mover.next
	return head

def convertArr2VLL(array: list) -> ChildListNode:
	if not array: return None
	head = ChildListNode(array[0])
	mover = head
	for i in range(1, len(array)):
		temp = ChildListNode(array[i])
		mover.child = temp
		mover = mover.child
	return head

def traverseVLL(vll):
	temp = vll
	output = []
	while temp:
		output.append(str(temp.data))
		# print(temp.data, end=" -> ")
		temp = temp.child
	# print("None")
	return output

def traverseLL(head: Node) -> list:
	temp = head
	output = []
	length = 0
	while temp:
		output.append(str(temp.data))
		length += 1
		temp = temp.next
	return output, length

def searchElement(head: Node, key: int):
	temp = head
	while temp:
		if temp.data == key: return True
		temp = temp.next
	return False

def deleteElementAtHead(head: Node) -> Node:
	if head is None: return head
	temp = head
	head = temp.next
	return head

def deleteElementAtTail(head: Node) -> Node:
	if head is None or head.next is None: return head
	temp = head
	while temp.next.next:
		temp = temp.next
	temp.next = None
	return head

def deleteElementAtK(head: Node, k: int) -> Node:
	if head is None: return head
	if k == 1:
		head = head.next
		return head
	temp = head
	cnt = 0
	prev = Node()
	while temp:
		cnt += 1
		if cnt == k:
			prev.next = prev.next.next
			break
		prev = temp
		temp = temp.next
	return head

def deleteElementValue(head: Node, value: int) -> Node:
	if head is None: return head
	if head.data == value:
		head = head.next
		return head
	temp = head
	cnt = 0
	prev = Node()
	while temp:
		if temp.data == value:
			prev.next = prev.next.next
			break
		prev = temp
		temp = temp.next
	return head

def insertAtHead(head: Node, value: int) -> Node:
	return Node(value, head)

def insertAtTail(head: Node, value: int) -> Node:
	if not head: return Node(value)
	temp = head
	while temp.next:
		temp = temp.next
	temp.next = Node(value)
	return head

def insertAtK(head: Node, value: int, k: int) -> Node:
	newNode = Node(value)
	if not head: return newNode
	if k == 1:
		newNode.next = head
		return newNode
	cnt = 0
	temp = head
	prev = Node()
	while temp:
		cnt += 1
		if cnt == k:
			prev.next = newNode
			newNode.next = temp
		prev = temp
		temp = temp.next
	return head

def insertBeforeValue(head: Node, el: int, value: int) -> Node:
	newNode = Node(value)
	if not head: return None
	if head.data == value:
		return Node(el, head)
	temp = head
	while temp.next:
		if temp.next.data == value:
			x = Node(el, temp.next)
			temp.next = x
			break
		temp = temp.next
	return head

def addTwoNumbers(head1: Node, head2: Node) -> Node:
	print(f">> LL 1: {' -> '.join(traverseLL(head1)[0])}")
	print(f">> LL 2: {' -> '.join(traverseLL(head2)[0])}")
	t1 = head1
	t2 = head2
	dummyNode = Node(-1)
	curr = dummyNode
	carry = 0
	while t1 or t2:
		sum = carry
		if t1:
			sum += t1.data
		if t2:
			sum += t2.data
		newNode = Node(sum % 10)
		carry = sum // 10
		curr.next = newNode
		curr = curr.next
		if t1: 
			t1 = t1.next
		if t2: 
			t2 = t2.next
	if carry:
		newNode = Node(carry)
		curr.next = newNode
	return dummyNode.next

def OddEvenBruteForce(head: Node) -> Node:
	if not head or not head.next: return head
	array = []
	temp = head
	while temp and temp.next:
		array.append(temp.data)
		temp = temp.next.next

	if temp: array.append(temp.data)
	temp = head.next
	while temp and temp.next:
		array.append(temp.data)
		temp = temp.next.next

	if temp: array.append(temp.data)
	i = 0
	temp = head
	while temp:
		temp.data = array[i]
		i += 1
		temp = temp.next
	return head

def OddEvenApp2(head: Node) -> Node:
	if not head or not head.next: return head
	odd = head
	even = head.next
	evenHead = head.next
	while (even and even.next ):
		odd.next = odd.next.next
		even.next = even.next.next
		odd = odd.next
		even = even.next
	odd.next = evenHead
	return head

def sortListBrute(head: Node) -> Node:
	print(">> Input List: ", ' -> '.join(traverseLL(head)[0]))
	temp = head
	cnt_0, cnt_1, cnt_2 = 0,0,0
	while temp:
		if temp.data == 0: cnt_0 += 1
		if temp.data == 1: cnt_1 += 1
		if temp.data == 2: cnt_2 += 1
		temp = temp.next
	temp = head
	while temp:
		if cnt_0 > 0:
			temp.data = 0
			cnt_0 -= 1
		elif cnt_1 > 0:
			temp.data = 1
			cnt_1 -= 1
		elif cnt_2 > 0:
			temp.data = 2
			cnt_2 -= 1
		temp = temp.next
	return head

def sortListOnePass(head: Node) -> Node:
	if not head or not head.next: return head
	temp = head
	zeroHead = Node(-1)
	oneHead = Node(-1)
	twoHead = Node(-1)
	zero = zeroHead
	one = oneHead
	two = twoHead
	while temp:
		if temp.data == 0:
			zero.next = temp
			zero = zero.next
		elif temp.data == 1:
			one.next = temp
			one = one.next
		else:
			two.next = temp
			two = two.next
		temp = temp.next
	zero.next = oneHead.next if oneHead.next else twoHead.next
	one.next = twoHead.next
	two.next = None

	newHead = zeroHead.next
	return newHead

def deleteNFromTail(head: Node, N: int) -> Node:
	print(">> Input List: ", ' -> '.join(traverseLL(head)[0]))
	cnt = 0
	temp = head
	while temp:
		cnt += 1
		temp = temp.next
	if cnt == N:
		newHead = head.next
		return newHead
	res = cnt - N
	temp = head
	while temp:
		res -= 1
		if res == 0: break
		temp = temp.next
	delNode = temp.next
	temp.next = temp.next.next
	return head

def deleteNFromTailApp2(head, N):
	if not head: return head
	fast = head
	for _ in range(N):
		fast = fast.next
	slow = head
	if not fast: return head.next

	while fast.next:
		slow = slow.next
		fast = fast.next
	slow.next = slow.next.next
	return head

def reverseListStack(head: Node) -> Node:
	print(f">> Input LL: ", ' -> '.join(traverseLL(head)[0]))
	st = Stack()
	temp = head
	while temp:
		st.push(temp.data)
		temp = temp.next
	temp = head
	while not st.is_empty():
		temp.data = st.pop()
		temp = temp.next
	return head

def reverseListIterative(head: Node) -> Node:
	temp = head
	prev = None
	while temp:
		front = temp.next
		temp.next = prev
		prev = temp
		temp = front
	return prev

def reverseListRecursive(head: Node) -> Node:
	if not head or not head.next: return head
	newHead = reverseListRecursive(head.next)
	front = head.next
	front.next = head
	head.next = None
	return newHead

def isPalindromeStack(head: Node) -> Node:
	print(f">> Input List: {' -> '.join(traverseLL(head)[0])}")
	if not head or not head.next: return True
	st = Stack()
	temp = head
	while temp:
		st.push(temp.data)
		temp = temp.next
	temp = head
	while temp:
		st_el = st.pop()
		if temp.data != st_el:
			return False
		else:
			temp = temp.next
	return True

def isPalindrome_V2(head: Node) -> Node:
	print(f">> Input List: {' -> '.join(traverseLL(head)[0])}")
	if not head or not head.next: return True
	slow = head
	fast = head
	while fast.next != None and fast.next.next != None:
		slow = slow.next
		fast = fast.next.next
	newHead = reverseListIterative(slow.next)
	first = head
	second = newHead
	while second:
		if first.data != second.data:
			reverseListIterative(newHead)
			return False
		first = first.next
		second = second.next
	reverseListIterative(newHead)
	return True

def addOne(head: Node) -> Node:
	print(f">> Input List: {' -> '.join(traverseLL(head)[0])}")
	head = reverseListIterative(head)
	temp = head
	carry = 1
	sum = 0
	while temp:
		sum = temp.data + carry
		temp.data = sum % 10
		carry = sum // 10
		if carry == 0: break
		temp = temp.next
	if carry:
		newNode = Node(carry)
		head = reverseListIterative(head)
		newNode.next = head
		return newNode
	else:
		head = reverseListIterative(head)
		return head
	
def addOneRecursive(head: Node) -> Node:
	print(f">> Input List: {' -> '.join(traverseLL(head)[0])}")
	carry = addOneRecursiveHelper(head)
	if carry:
		newNode = Node(carry, head)
		return newNode
	return head

def addOneRecursiveHelper(temp: Node):
	if not temp: return 1
	carry = addOneRecursiveHelper(temp.next)
	sum = temp.data + carry
	temp.data = sum % 10
	carry = sum // 10
	return carry

def findIntersection_v1(head1: Node, head2: Node) -> Node:
	print(f">> Input List 1: {' -> '.join(traverseLL(head1)[0])}")
	print(f">> Input List 2: {' -> '.join(traverseLL(head2)[0])}")
	mpp = {}
	temp = head1
	while temp:
		mpp[temp] = 1
		temp = temp.next
	
	temp = head2
	while temp:
		if temp in mpp:
			return temp
		temp = temp.next
	return None

def findIntersection_v2(head1: Node, head2: Node) -> Node:
	temp1, temp2 = head1, head2
	n1, n2 = 0, 0

	while temp1:
		temp1 = temp1.next
		n1 += 1

	while temp2:
		temp2 = temp2.next
		n2 += 1

	temp1, temp2 = head1, head2
	for _ in range(abs(n1 - n2)):
		if n1 > n2: temp1 = temp1.next
		elif n2 > n1: temp2 = temp2.next
	while temp1 != temp2:
		temp1 = temp1.next
		temp2 = temp2.next
	return temp1

def findIntersection_v3(head1: Node, head2: Node) -> Node:
	if not head1 or not head2: return None
	t1, t2 = head1, head2
	while t1 != t2:
		t1 = t1.next
		t2 = t2.next
		if t1 == t2: return t1
		if not t1: t1 = head2
		if not t2: t2 = head1
	return t1

def getMiddle_v1(head: Node) -> Node:
	if not head or not head.next: return head
	print(f">> Input List: {' -> '.join(traverseLL(head)[0])}")
	# Pass 1: to get the length of the list
	length = 0
	temp = head
	while temp:
		length += 1
		temp = temp.next
	if length & 1:
		mid = getMiddleHelper(head, (length+1)//2)
	else:
		mid = getMiddleHelper(head, (length//2)+1)
	return mid

def getMiddleHelper(head: Node, node: int) -> Node:
	cnt = 0
	temp = head
	while temp:
		cnt += 1
		if cnt == node:
			return temp
		temp = temp.next
	return temp

def getMiddle_v2(head: Node) -> Node:
	print(f">> Input List: {' -> '.join(traverseLL(head)[0])}")
	if not head or not head.next: return head
	slow = head
	fast = head # fast = head.next for returning mid 1 else it will return mid 2
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow

def detectCycle_v1(head: Node) -> bool:
	mpp = {}
	temp = head
	while temp:
		if temp in mpp:
			return True
		mpp[temp] = 1
		temp = temp.next
	return False

def detectCycle_v2(head: Node) -> bool:
	if not head or not head.next: return head
	slow, fast = head, head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast: return True
	return False

def getLoopLength_v1(head: Node) -> int:
	if not head or not head.next: return 0
	mpp = {}
	temp = head
	timer = 1
	while temp:
		if temp in mpp:
			val = mpp[temp]
			return (timer-val)
		mpp[temp] = timer
		timer += 1
		temp = temp.next
	return 0

def getLoopLength_v2(head: Node) -> bool:
	if not head or not head.next: return head
	slow, fast = head, head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast: return findLength(slow, fast)
	return False

def findLength(slow, fast):
	cnt = 1
	fast = fast.next
	while slow != fast:
		cnt += 1
		fast = fast.next
	return cnt

def deleteMid_v1(head: Node) -> Node:
	if not head or not head.next: return None
	# Pass 1: Finding the length of the list
	length = 0
	temp = head
	while temp:
		length += 1
		temp = temp.next
	mid = length // 2
	# print("Length of the list: ", length, " Mid is at : ", mid)
	# Pass 2: Reaching to the node before the mid.
	temp = head
	while temp:
		mid -= 1
		if not mid:
			temp.next = temp.next.next
			break
		temp = temp.next
	return head

def deleteMid_v2(head: Node) -> Node:
	if not head or not head.next: return None
	temp = head
	slow, fast = head, head
	fast = fast.next.next
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	slow.next = slow.next.next
	return head

def getStartOfLoop_v1(head: Node) -> Node:
	if not head or not head.next: return None
	mpp = {}
	temp = head
	while temp:
		if temp in mpp:
			return temp
		mpp[temp] = 1
		temp = temp.next
	return None

def getStartOfLoop_v2(head: Node) -> Node:
	if not head or not head.next: return head
	slow, fast = head, head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			slow = head
			while slow != fast:
				slow = slow.next
				fast = fast.next
			return slow
	return None

def getKNode(temp: Node, k: int) -> Node:
	k -= 1
	while temp and k > 0:
		k -= 1
		temp = temp.next
	return temp

def reverseNodeInK(head: Node, k: int) -> Node:
	print(f">> Input List: {' -> '.join(traverseLL(head)[0])}")
	print(f">> K : {k}")
	temp = head
	prevNode = None

	while temp:
		kNode = getKNode(temp, k)
		if not kNode:  
			break

		nextNode = kNode.next
		kNode.next = None
		reversedHead = reverseListIterative(temp)  

		if prevNode:
			prevNode.next = reversedHead
		else:
			head = reversedHead  

		prevNode = temp  
		temp.next = nextNode 
		temp = nextNode  

	return head

def mergeListsNaive(head1: Node, head2: Node) -> Node:
	print(f">> Input List 1: {' -> '.join(traverseLL(head1)[0])}")
	print(f">> Input List 2: {' -> '.join(traverseLL(head2)[0])}")
	array = []
	temp = head1
	while temp:
		array.append(temp.data)
		temp = temp.next
	# print("Array: ", array)
	temp = head2
	while temp:
		array.append(temp.data)
		temp = temp.next
	newHead = convertArr2LL(array.sort())
	return newHead

def mergeListsOptimized(head1: Node, head2: Node) -> Node:
	t1, t2 = head1, head2
	
	dNode = Node(-1)
	temp = dNode

	while t1 and t2:
		if t1.data < t2.data:
			temp.next = t1
			temp = t1
			t1 = t1.next
		else:
			temp.next = t2
			temp = t2
			t2 = t2.next
	if t1: temp.next = t1
	else: temp.next = t2
	return dNode.next

def FlattenList(head: Node):
	array = []
	temp = head
	while temp:
		array.append(temp.data)
		t2 = temp.child
		while t2: 
			array.append(t2.data)
			t2 = t2.child
		temp = temp.next
	array.sort()
	newHead = convertArr2VLL(array)
	return newHead	

def FlattenListOptimized(head: ChildListNode):
	if not head or not head.next: return head
	mergedHead = FlattenListOptimized(head.next)
	return Merge2List(head, mergedHead)

def Merge2List(head1, head2):
	dNode = ChildListNode(-1)
	temp = dNode
	t1, t2 = head1, head2
	while t1 and t2:
		if t1.data < t2.data:
			temp.child = t1
			temp = t1
			t1 = t1.child
		else:
			temp.child = t2
			temp = t2
			t2 = t2.child
		temp.next = None
	if t1: temp.child = t1
	else: temp.child = t2
	return dNode.child

def mergeKSortedListsNaive(lists: Node) -> Node:
	array = []
	for i in range(len(lists)):
		temp = lists[i]
		while temp:
			array.append(temp.data)
			temp = temp.next	
	array.sort()
	return convertArr2LL(array)

def mergeKSortedListsOptimized(lists: Node) -> Node:
	head = lists[0]
	for i in range(1, len(lists)):
		head = mergeListsOptimized(head, lists[i])
	return head

def mergeKSortedListPQ(lists: Node) -> Node:
	minH = []
	heapify(minH)
	for i in range(len(lists)):
		temp = lists[i]
		heappush(minH, (temp.data, temp))

	dNode = Node(-1)
	temp = dNode
	while minH:
		val, node = heappop(minH)
		temp.next = node
		if node.next:
			heappush(minH, (node.next.data, node.next))
		temp = temp.next
	return dNode.next

def sortListNaive(head: Node) -> Node:
	if not head or not head.next: return head
	temp = head
	array = []
	while temp:
		array.append(temp.data)
		temp = temp.next
	array.sort()
	return convertArr2LL(array)

def findMid(head):
	if not head or not head.next: return head
	slow = head
	fast = head.next # fast = head.next for returning mid 1 else it will return mid 2
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow

def sortListMerge(head: Node) -> Node:
	if not head or not head.next: return head
	mid = findMid(head)
	leftHead, rightHead = head, mid.next
	mid.next = None
	leftHead = sortListMerge(leftHead)
	rightHead = sortListMerge(rightHead)
	return mergeListsOptimized(leftHead, rightHead)

def copyListNaive(head: RandomNode) -> RandomNode:
	temp = head
	mpp = {}

	# Step 1: Create copies of each node
	while temp is not None:
		newNode = Node(temp.data)
		mpp[temp] = newNode
		temp = temp.next

	temp = head
	# Step 2: Connect the next and random
	while temp is not None:
		copyNode = mpp[temp]
		copyNode.next = mpp.get(temp.next, None)
		copyNode.random = mpp.get(temp.random, None)
		temp = temp.next
	return mpp[head]

def copyListOptimized(head: RandomNode) -> RandomNode:
	if not head or not head.next: return head
	# Step 1: insert copy in between nodes
	insertCopyNode(head)
	# Step 2: Connect Random Pointers
	connectRandomPointers(head)
	# Step 3: Get deep copy list
	return deepCopyList(head)

def insertCopyNode(head: RandomNode) -> RandomNode:
	temp = head
	while temp:
		nextElement = temp.next
		copyNode = RandomNode(temp.data)
		copyNode.next = nextElement
		temp.next = copyNode
		temp = nextElement

def connectRandomPointers(head: RandomNode) -> RandomNode:
	temp = head
	while temp:
		copyNode = temp.next
		if temp.random: copyNode.random = temp.random.next
		else: copyNode.random = None
		temp = temp.next.next

def deepCopyList(head: RandomNode) -> RandomNode:
	temp = head
	dNode = RandomNode(-1)
	res = dNode
	while temp:
		res.next = temp.next
		res = res.next
		temp.next = temp.next.next
		temp = temp.next
	return dNode.next