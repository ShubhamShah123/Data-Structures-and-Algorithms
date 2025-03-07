import DoublyLinkedListFunctions as dll

array = [1,3,2,4,6,5,7]


head = dll.convertArr2DLL(array)
print(f"1. Head of DLL: {head.data}")

output = dll.traverseDLL(head)
print(f"\n2. DLL traversal: {' <-> '.join(output)}")

head = dll.convertArr2DLL(array)
delHead = dll.deleteHead(head)
output = dll.traverseDLL(delHead)
print(f"\n3. DLL after deleting head: {' <-> '.join(output)}" )

head = dll.convertArr2DLL(array)
delHead = dll.deleteTail(head)
output = dll.traverseDLL(delHead)
print(f"\n4. DLL after deleting tail: {' <-> '.join(output)}" )

head = dll.convertArr2DLL(array)
k = 4
delHead = dll.deleteAtK(head, k)
output = dll.traverseDLL(delHead)
print(f"\n5. DLL after deleting at K={k}: {' <-> '.join(output)}" )

head = dll.convertArr2DLL(array)
value = 1
delHead = dll.deleteValue(head, value)
output = dll.traverseDLL(delHead)
print(f"\n6. DLL after deleting value={value}: {' <-> '.join(output)}" )


head = dll.convertArr2DLL(array)
value = 10
delHead = dll.insertBeforeHead(head, value)
output = dll.traverseDLL(delHead)
print(f"\n7. DLL after inserting value={value} before head: {' <-> '.join(output)}" )

head = dll.convertArr2DLL(array)
value = 20
delHead = dll.insertBeforeTail(head, value)
output = dll.traverseDLL(delHead)
print(f"\n8. DLL after inserting value={value} before tail: {' <-> '.join(output)}" )

head = dll.convertArr2DLL(array)
value = 30
k=5
delHead = dll.insertBeforeK(head, k, value)
output = dll.traverseDLL(delHead)
print(f"\n9. DLL after inserting value={value} before k={k}: {' <-> '.join(output)}" )

head = dll.convertArr2DLL(array)
value = 40
el=5
delHead = dll.insertBeforeValue(head, el, value)
output = dll.traverseDLL(delHead)
print(f"\n10. DLL after inserting value={value} before element={el}: {' <-> '.join(output)}" )

head = dll.convertArr2DLL(array)
value = 50
newHead = dll.insertAfterHead(head, value)
output = dll.traverseDLL(newHead)
print(f"\n11. DLL after inserting value={value} after HEAD: {' <-> '.join(output)}")

head = dll.convertArr2DLL(array)
value = 60
newTail = dll.insertAfterTail(head, value)
output = dll.traverseDLL(newTail)
print(f"\n12. DLL after inserting value={value} after TAIL: {' <-> '.join(output)}")


head = dll.convertArr2DLL(array)
value = 70
k = 3
newHead = dll.insertAfterK(head, value, k)
output = dll.traverseDLL(newHead)
print(f"\n13. DLL after inserting value={value} after K={k}: {' <-> '.join(output)}")

head = dll.convertArr2DLL(array)
value = 80
el = 1
newHead = dll.insertAfterValue(head, value, el)
output = dll.traverseDLL(newHead)
print(f"\n14. DLL after inserting value={value} after el={el}: {' <-> '.join(output)}")

head = dll.convertArr2DLL(array)
newHead = dll.reverseUsingStack(head)
output = dll.traverseDLL(newHead)
print(f"\n15. Reversed DLL using stack: {' <-> '.join(output)}")


head = dll.convertArr2DLL(array)
newHead = dll.reverseOnePass(head)
output = dll.traverseDLL(newHead)
print(f"\n16. Reversed DLL in One Pass: {' <-> '.join(output)}")

print("\n17. Delete all occurence of given key from the dll.")
array = [10, 4, 20, 10, 6, 10]
head = dll.convertArr2DLL(array)
key = 10
newHead = dll.deleteAllOccurence(head, key)
output = dll.traverseDLL(newHead)
print(f">> Output: {' <-> '.join(output)}")

print("\n18. Get all pairs with the given sum.")
array = [0,1,2,3,4,5,6,7,8,9,10]
sum = 10
head = dll.convertArr2DLL(array)
output_v1 = dll.getParisWithSum_v1(head, sum)
print(f">> Output V1: {output_v1}")
output_v2 = dll.getParisWithSum_v2(head, sum)
print(f">> Output V2: {output_v2}")

print("\n19. Remove duplicates.")
array = [1,2,3,4]
head = dll.convertArr2DLL(array)
output = dll.removeDuplicates(head)
print(f">> Output V1: {' <-> '.join(dll.traverseDLL(output))}")
