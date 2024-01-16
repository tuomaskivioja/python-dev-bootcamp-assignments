def ispalindrome(node):
    curr = node
    rev = []

    while curr is not None:
        rev.append(curr.value)
        curr = curr.next

    while node is not None:
        i = rev.pop()
        if node.value != i:
            return False

        node = node.next

    return True
