def reverse_singly_linked_list_iterative(head):
    if not (head is None or head.next is None):
        current_node = head
        next_node = current_node.next
        head.next = None

        while next_node is not None:
            next_next_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = next_next_node

        head = current_node

    return head


def reverse_singly_linked_list_recursive(head):
    if not (head is None or head.next is None):
        def _reverse_sll(node):
            nonlocal head
            if node.next is None:
                head.next = None
                head = node
            else:
                returned_node = _reverse_sll(node.next)
                returned_node.next = node
            return node

        _reverse_sll(head)
    return head