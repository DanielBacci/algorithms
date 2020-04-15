def insertNodeAtPosition(head, data, position):
    item = head
    for index in range(1, position):
        item = item.next

    node = SinglyLinkedListNode(data)
    node.next = item.next
    item.next = node
    return head
    
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if (head == None):
        return node
    elif (data < head.data):
        node.next = head
        head.prev = node
        return node
    else:
        node = sortedInsert(head.next, data)
        head.next = node 
        node.prev = head
        return head
