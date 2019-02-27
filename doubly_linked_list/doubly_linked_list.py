"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        if self.head is not None:
            temp = self.head
            self.head.next.prev = None
            self.head = self.head.next
            return temp.value

    def add_to_tail(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        if self.tail is not None:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return temp.value

    def move_to_front(self, node):
        temp = self.head
        while temp:
            if node.value == temp.value:
                break
            temp = temp.next
        temp.delete()
        self.add_to_head(temp.value)

    def move_to_end(self, node):
        temp = self.head
        while temp:
            if node.value == temp.value:
                break
            temp = temp.next
        temp.delete()
        self.add_to_tail(temp.value)

    def delete(self, node):
        temp = self.head
        while temp:
            if node == temp:
                break
            temp = temp.next
            print(temp)

        print("Temp", temp.value)
        if not temp.prev and not temp.next:
            temp.delete()
            self.head = None
            self.tail = None
        elif not temp.prev:
            self.head = temp.next
            temp.delete()
        else:
            temp.delete()

    def get_max(self):
        current = self.head
        max_val = current.value

        while current.next is not None:
            first_val = current.value
            current = current.next
            if current.value > first_val:
                max_val = current.value

        return max_val
