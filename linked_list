def insertNodeAtPosition(head, data, position):
    item = head
    for index in range(1, position):
        item = item.next

    node = SinglyLinkedListNode(data)
    node.next = item.next
    item.next = node
    return head
    
