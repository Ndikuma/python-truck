class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.succeeding

    # Add to end
    def push(self, value):
        node = Node(value)

        if not self.head:
            self.head = self.tail = node
        else:
            node.previous = self.tail
            self.tail.succeeding = node
            self.tail = node

        self.length += 1

    # Remove from end
    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")

        value = self.tail.value
        self.tail = self.tail.previous

        if self.tail:
            self.tail.succeeding = None
        else:
            self.head = None

        self.length -= 1
        return value

    # Add to front
    def unshift(self, value):
        node = Node(value)

        if not self.head:
            self.head = self.tail = node
        else:
            node.succeeding = self.head
            self.head.previous = node
            self.head = node

        self.length += 1

    # Remove from front
    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")

        value = self.head.value
        self.head = self.head.succeeding

        if self.head:
            self.head.previous = None
        else:
            self.tail = None

        self.length -= 1
        return value

    # Delete first occurrence
    def delete(self, value):
        current = self.head

        while current:
            if current.value == value:

                if current.previous:
                    current.previous.succeeding = current.succeeding
                else:
                    self.head = current.succeeding

                if current.succeeding:
                    current.succeeding.previous = current.previous
                else:
                    self.tail = current.previous

                self.length -= 1
                return

            current = current.succeeding

        raise ValueError("Value not found")