import LinkedListFunctions as ll
from Node import ChildListNode, RandomNode, Node

array = [1,3,4,2,5,6,0]
def number_to_reversed_array(num: int) -> list:
    return [int(digit) for digit in str(abs(num))[::-1]]

def printClonedLinkedList(head):
    while head is not None:
        data = head.data
        random_data = head.random.data if head.random else "nullptr"
        next_data = head.next.data if head.next else "nullptr"
        
        print(f"Data: {data}, Random: {random_data}, Next: {next_data}")
        
        head = head.next

head = ll.convertArr2LL(array)
print(f"1. Converting array to linekd list: {head.data}")

traverse, length = ll.traverseLL(head)
print(f"\n2. Traversing the linked list: {' -> '.join(traverse)}")

print(f"\n3. Length of linked list: {length}")

key = 9
print(f"\n4. Key: {key} present in linked list? --> {ll.searchElement(head, key)}")

head = ll.convertArr2LL(array)
newHead = ll.deleteElementAtHead(head)
print(f"\n5. New head after deleting the head --> {newHead.data} : {' -> '.join(ll.traverseLL(newHead)[0])}")

head = ll.convertArr2LL(array)
newHead = ll.deleteElementAtTail(head)
print(f"\n6. Linked List after deleting the tail : {' -> '.join(ll.traverseLL(newHead)[0])}")

index = 2
head = ll.convertArr2LL(array)
newHead = ll.deleteElementAtK(head, index)
print(f"\n7. Linked List after deleting at index: {index}: {' -> '.join(ll.traverseLL(newHead)[0])}")

value = 3
head = ll.convertArr2LL(array)
newHead = ll.deleteElementValue(head, value)
print(f"\n8. Linked List after deleting element with value: {value}: {' -> '.join(ll.traverseLL(newHead)[0])}")

value = 10
head = ll.convertArr2LL(array)
newHead = ll.insertAtHead(head, value)
ll_new = ' -> '.join(ll.traverseLL(newHead)[0])
print(f"\n9. Linked List after inserting element at HEAD with value: {value}: {ll_new}")

value = 10
head = ll.convertArr2LL(array)
newHead = ll.insertAtTail(head, value)
ll_new = ' -> '.join(ll.traverseLL(newHead)[0])
print(f"\n10. Linked List after inserting element at TAIL with value: {value}: {ll_new}")

index = 3
value = 10
head = ll.convertArr2LL(array)
newHead = ll.insertAtK(head, value, index)
ll_new = ' -> '.join(ll.traverseLL(newHead)[0])
print(f"\n11. Linked List after inserting element at index: {index} with value: {value}: {ll_new}")

el = 1
value = 10
head = ll.convertArr2LL(array)
newHead = ll.insertBeforeValue(head, value, el)
ll_new = ' -> '.join(ll.traverseLL(newHead)[0])
print(f"\n12. Linked List after inserting element before {el} with value: {value}: {ll_new}")

print("\n17. Adding 2 linked lists: ")
n1 = number_to_reversed_array(53)
n2 = number_to_reversed_array(9954)
head1 = ll.convertArr2LL(n1)
head2 = ll.convertArr2LL(n2)
output = ll.addTwoNumbers(head1, head2)
result = ll.traverseLL(output)[0]
print(f">> Result: {' -> '.join(result)}")

print("\n18(i). Odd Even Linked List:")
head = ll.convertArr2LL(array)
output = ll.OddEvenBruteForce(head)
result, _ = ll.traverseLL(output)
print(f">> Output: {' -> '.join(result)}")

print("\n18(ii). Odd Even Linked List:")
head = ll.convertArr2LL(array)
output = ll.OddEvenApp2(head)
result, _ = ll.traverseLL(output)
print(f">> Output: {' -> '.join(result)}")

print("\n19(i). Sorting 0s, 1s and 2s")
array = [1,0,2,1,0,2,1]
head = ll.convertArr2LL(array)
output = ll.sortListBrute(head)
result, _ = ll.traverseLL(output)
print(f">> Output: {' -> '.join(result)}")

print("\n19(ii). Sorting 0s, 1s and 2s")
array = [1,0,2,1,0,2,1,0]
head = ll.convertArr2LL(array)
output = ll.sortListOnePass(head)
result, _ = ll.traverseLL(output)
print(f">> Output: {' -> '.join(result)}")

print("\n20(i). Deleting Nth from end.")
array = [1,2,3,4,5]
head = ll.convertArr2LL(array)
N = 2
output = ll.deleteNFromTail(head, N)
result, _ = ll.traverseLL(output)
print(f">> Deleting {N}th element from the tail : {' -> '.join(result)}")

array = [1,2,3,4,5]
head = ll.convertArr2LL(array)
N = 5
output2 = ll.deleteNFromTailApp2(head, N)
result2, _ = ll.traverseLL(output2)

print("\n20(ii) Deleting Nth from end approach 2:")
print(f">> Deleting {N}th element from the tail : {' -> '.join(result2)}")

print("\n21(i). Reversing Linked List using Stack.")
array = [1,2,3,4,5]
head = ll.convertArr2LL(array)
output = ll.reverseListStack(head)
res, _ = ll.traverseLL(output)
print(f">> Reversed LL: {' -> '.join(res)}")


print("\n21(ii). Reversing Linked List using Iteration.")
array = [1,2,3,4,5]
head = ll.convertArr2LL(array)
print(f">> Input LL: ", ' -> '.join(ll.traverseLL(head)[0]))
output = ll.reverseListIterative(head)
res, _ = ll.traverseLL(output)
print(f">> Reversed LL: {' -> '.join(res)}")

print("\n21(iii). Reversing Linked List using Recursion.")
array = [1,2,3,4,5]
head = ll.convertArr2LL(array)
output = ll.reverseListRecursive(head)
res, _ = ll.traverseLL(output)
print(f">> Reversed LL: {' -> '.join(res)}")

print("\n22(i). Check if given linked list is palindrome or not.")
array = [1,2,3,2,1]
head = ll.convertArr2LL(array)
output = ll.isPalindromeStack(head)
print(f">> Output: ", output)

print("\n22(ii). Check if given linked list is palindrome or not.")
array = [1,2,3,2,1]
head = ll.convertArr2LL(array)
output = ll.isPalindrome_V2(head)
print(f">> Output: ", output)

print("\n23(i). Adding 1 to the linkedlist.")
array = [9,9]
head = ll.convertArr2LL(array)
output = ll.addOne(head)
result, _ = ll.traverseLL(output)
print(f">> Result: {' -> '.join(result)}")

print("\n23(ii). Adding 1 to the linkedlist recursive.")
array = [9,9,9,9]
head = ll.convertArr2LL(array)
output = ll.addOneRecursive(head)
result, _ = ll.traverseLL(output)
print(f">> Result: {' -> '.join(result)}")

print("\n24(i). Finding intersection of Y linked list(Naive).")
common_node = Node(4, Node(6, Node(2)))
head1 = Node(3, Node(1, common_node))
head2 = Node(1, Node(2, Node(4, Node(5, common_node))))
output = ll.findIntersection_v1(head1, head2)
result, _ = ll.traverseLL(output)
print(f">> Result: {' -> '.join(result)}")

print("\n24(ii). Finding Intersection of Y Linked list(Length):")
output2 = ll.findIntersection_v2(head1, head2)
result, _ = ll.traverseLL(output2)
print(f">> Result: {' -> '.join(result)}")

print("\n24(iii). Finding Intersection of Y Linked list(Change the t1, t2):")
output3 = ll.findIntersection_v3(head1, head2)
result, _ = ll.traverseLL(output3)
print(f">> Result: {' -> '.join(result)}")

print("\n25(i). Get the middle of the list.")
array = [1,2,3,4,5]
head = ll.convertArr2LL(array)
output = ll.getMiddle_v1(head)
print(f">> Result: {output, output.data}")

print("\n25(ii). Get the middle of the list.")
array = [1,2,3,4,5]
head = ll.convertArr2LL(array)
output = ll.getMiddle_v2(head)
print(f">> Result: {output, output.data}")

print("\n26(i). Detect the loop (Naive - Brute Force).")
ninth = Node(9)
third = Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, ninth))))))
ninth.next = third
head = Node(1, Node(2, third))
print(">> Input List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> (back to) 3")
output = ll.detectCycle_v1(head)
print(f">> Output: {output}")

print("\n26(ii) Detecting Cycle V2")
ninth = Node(9)
third = Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, ninth))))))
head = Node(1, Node(2, third))
print(">> Input List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9")

output = ll.detectCycle_v2(head)
print(f">> Output: {output}")


print("\n27(i). Length of the loop(Naive-Brute Force).")
ninth = Node(9)
third = Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, ninth))))))
ninth.next = third
head = Node(1, Node(2, third))
print(">> Input List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> (back to) 3")
output = ll.getLoopLength_v1(head)
print(f">> Output: {output}")

print("\n27(ii). Length of the loop(Tortoise hare)")
print(">> Input List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> (back to) 3")
output = ll.getLoopLength_v2(head)
print(f">> Output: {output}")

print("\n28(i). Deleting the mid of the (Naive Method).")
oHead = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(f">> Inpust List: Odd Length: {' -> '.join(ll.traverseLL(oHead)[0])}")
newOdd = ll.deleteMid_v1(oHead)
oRes, _ = ll.traverseLL(newOdd)
print(f">> Output: {' -> '.join(oRes)}")

eHead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
print(f">> Inpust List: Even Length: {' -> '.join(ll.traverseLL(eHead)[0])}")
newEven = ll.deleteMid_v1(eHead)
eRes, _ = ll.traverseLL(newEven)
print(f">> Output: {' -> '.join(eRes)}")

print("\n28(ii). Deleting the mid of the (Optimized).")
oHead = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(f">> Inpust List: Odd Length: {' -> '.join(ll.traverseLL(oHead)[0])}")
newOdd = ll.deleteMid_v2(oHead)
oRes, _ = ll.traverseLL(newOdd)
print(f">> Output: {' -> '.join(oRes)}")

eHead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
print(f">> Inpust List: Even Length: {' -> '.join(ll.traverseLL(eHead)[0])}")
newEven = ll.deleteMid_v2(eHead)
eRes, _ = ll.traverseLL(newEven)
print(f">> Output: {' -> '.join(eRes)}")

print("\n29(i). Starting point of the loop(Naive-Brute Force).")
ninth = Node(9)
third = Node(15, Node(4, Node(13, Node(6, Node(7, Node(8, ninth))))))
ninth.next = third
head = Node(1, Node(2, Node(3, third)))
print(">> Input List: 1 -> 2 -> 3 -> 15 -> 4 -> 13 -> 6 -> 7 -> 8 -> 9 -> (back to) 3")
output = ll.getStartOfLoop_v1(head)
print(f">> Output: {output.data, output}")

print("\n29(ii). Starting point of the loop(Optimized).")
print(">> Input List: 1 -> 2 -> 3 -> 15 -> 4 -> 13 -> 6 -> 7 -> 8 -> 9 -> (back to) 3")
output = ll.getStartOfLoop_v2(head)
print(f">> Output: {output.data, output}")

print("\n30. Reverse in K-Group.")
array = [1,2,3,4,5,6,7,8,9,10]
head = ll.convertArr2LL(array)
k = 4
output = ll.reverseNodeInK(head, k)
res, _ = ll.traverseLL(output)
print(f">> Output: {' -> '.join(res)}")

print("\n31(i). Merging list - Naive.")
a1 = [2,4,6,8]
a2 = [1,3,3,5,11,13]
head1 = ll.convertArr2LL(a1)
head2 = ll.convertArr2LL(a2)
output = ll.mergeListsNaive(head1, head2)
res, _ = ll.traverseLL(output)
print(f">> Merged List: {' -> '.join(res)}")

print("\n31(ii). Merging list - Optimized.")
a1 = [1,2,3,4]
a2 = [1,2,3,4]
head1 = ll.convertArr2LL(a1)
head2 = ll.convertArr2LL(a2)
print(f">> Input List 1: {' -> '.join(ll.traverseLL(head1)[0])}")
print(f">> Input List 2: {' -> '.join(ll.traverseLL(head2)[0])}")
output = ll.mergeListsOptimized(head1, head2)
res, _ = ll.traverseLL(output)
print(f">> Merged List: {' -> '.join(res)}")

print("\n32. Flatenning the linked list.")
fifth = ChildListNode(5, ChildListNode(6, ChildListNode(8)))
fourth = ChildListNode(4, ChildListNode(9), fifth)
third = ChildListNode(1, ChildListNode(7, ChildListNode(11, ChildListNode(12))), fourth)
second = ChildListNode(2, ChildListNode(10), third)
first = ChildListNode(3, None, second)

head = first

output = ll.FlattenList(head)
res = ll.traverseVLL(output)
print(f">> Flattened List: {' -> '.join(res)}")

fifth = ChildListNode(5, ChildListNode(6, ChildListNode(8)))
fourth = ChildListNode(4, ChildListNode(9), fifth)
third = ChildListNode(1, ChildListNode(7, ChildListNode(11, ChildListNode(12))), fourth)
second = ChildListNode(2, ChildListNode(10), third)
first = ChildListNode(3, None, second)

head = first
output = ll.FlattenListOptimized(head)
res = ll.traverseVLL(output)
print(f">> Flattened List Optimized: {' -> '.join(res)}")

print("\n33. Merge K-sorted linkedLists")
head0 = Node(2, Node(4, Node(6)))
head1 = Node(1, Node(5))
head2 = Node(1, Node(1, Node(3, Node(7))))
head3 = Node(8)
lists = [head0, head1, head2, head3]

for i in range(len(lists)):
    print(f">> Input List {i}: {' -> '.join(ll.traverseLL(lists[i])[0])}")

output = ll.mergeKSortedListsNaive(lists)
res, _ = ll.traverseLL(output)
print(f">> Naive Merging: {' -> '.join(res)}")
head0 = Node(2, Node(4, Node(6)))
head1 = Node(1, Node(5))
head2 = Node(1, Node(1, Node(3, Node(7))))
head3 = Node(8)
lists = [head0, head1, head2, head3]
output = ll.mergeKSortedListsOptimized(lists)
res, _ = ll.traverseLL(output)
print(f">> Optimized Merging: {' -> '.join(res)}")

head0 = Node(2, Node(4, Node(6)))
head1 = Node(1, Node(5))
head2 = Node(1, Node(1, Node(3, Node(7))))
head3 = Node(8)
lists = [head0, head1, head2, head3]
output = ll.mergeKSortedListPQ(lists)
res, _ = ll.traverseLL(output)
print(f">> PQ Merging: {' -> '.join(res)}")

print("\n34. Sort the list.")
head = Node(3, Node(4, Node(7, Node(1, Node(5, Node(6, Node(2)))))))
print(f">> Input List: {' -> '.join(ll.traverseLL(head)[0])}")
output = ll.sortListNaive(head)
res, _ = ll.traverseLL(output)
print(f">> Output List Naive: {' -> '.join(res)}")

head = Node(3, Node(4, Node(7, Node(1, Node(5, Node(6, Node(2)))))))
output = ll.sortListMerge(head)
res, _ = ll.traverseLL(output)
print(f">> Output List Merge sort: {' -> '.join(res)}")

print("\n35. Copying a list with random pointers. ")

head = RandomNode(7)
first = RandomNode(13)
second = RandomNode(11)
third = RandomNode(10)
fourth = RandomNode(1)

head.next = first
head.random = second
first.next = second
first.random = head
second.next = third
second.random = None
third.next = fourth
third.random = first
fourth.next = None
fourth.random = second

output = ll.copyListNaive(head)
print(">> Naive Output")
printClonedLinkedList(output)

head = RandomNode(7)
first = RandomNode(13)
second = RandomNode(11)
third = RandomNode(10)
fourth = RandomNode(1)

head.next = first
head.random = second
first.next = second
first.random = head
second.next = third
second.random = None
third.next = fourth
third.random = first
fourth.next = None
fourth.random = second

output = ll.copyListOptimized(head)
print(">> Optimized Output:")
printClonedLinkedList(output)
