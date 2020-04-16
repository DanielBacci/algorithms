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

def reverse(head):
    if not head:
        return head
    
    head.next, head.prev = head.prev, head.next
    if not head.prev:
        return head

    return reverse(head.prev)

def findMergeNode(Ahead, Bhead):
    a_head, b_head = Ahead, Bhead
    while a_head != b_head:
        a_head, b_head = a_head.next or Ahead, b_head.next or Bhead
    return a_head.data
