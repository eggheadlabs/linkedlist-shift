# Shift a singly-linked-list by k steps. The shift operation should be done in place withouot needing extra space.
# Positive k means forward shift; negative k means backward shift. For the case of k larger than the actual length of the llist, shift operation is cycling the llist with a net effective offset.
# Example:  original llist:     0 -> 1 -> 2 -> 3 -> 4 -> 5
#           shifted by k=2:     4 -> 5 -> 0 -> 1 -> 2 -> 3
#           shifted by k=-2:    2 -> 3 -> 4 -> 5 -> 0 -> 1
#           shifted by k=8:     4 -> 5 -> 0 -> 1 -> 2 -> 3  (same as k=2 case, the net effective shift is 2)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def traverse(self):
        node = self.head
        length = 1
        while node.next is not None:
            length += 1
            node = node.next
        return node, length

    def print_llist(self):
        node = self.head
        while node is not None:
            print(str(node.data) + ' -> ', end='', flush=True)
            node = node.next
        print('None')

    def shift(self, k):
        tail, length = self.traverse()
        offset = abs(k) % length
        if offset != 0:
            new_tail_position = length - offset if k > 0 else offset

            # find the new_tail
            new_tail = self.head
            for i in range(1, new_tail_position):   # counting start at the first node as 1 (rather 0)
                new_tail = new_tail.next

            tail.next = self.head
            self.head = new_tail.next
            new_tail.next = None


# Preparation: create the SinglyLinkedList according to a given input
s = [0, 1, 2, 3, 4, 5]
sll = SinglyLinkedList()
for x in reversed(s): sll.push(x)

# shift steps
k = 2

# before shift
sll.print_llist()

# shift
sll.shift(k)

# after shift
sll.print_llist()