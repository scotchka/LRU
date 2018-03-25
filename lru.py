class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return f'Node({repr(self.data)})'


class DLL(object):
    def __init__(self):
        """Circular doubly linked list with a sentinal node."""

        self.terminal = Node('terminal')
        self.terminal.next = self.terminal
        self.terminal.prev = self.terminal

    def add(self, node, next=None):
        """Add new node before existing node, defaulting to the sentinal."""

        if next is None:
            next = self.terminal

        prev = next.prev

        prev.next = node
        node.prev = prev

        node.next = next
        next.prev = node

    @staticmethod
    def remove(node):
        """Remove node from linked list."""
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    @property
    def head(self):
        return self.terminal.prev

    @property
    def tail(self):
        return self.terminal.next


class LRU(dict):
    def __init__(self, maxsize, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxsize = maxsize
        self._dll = DLL()
        self._dict = {}

    def __setitem__(self, key, value):
        if key in self._dict:
            node = self._dict[key]
            self._dll.remove(node)

        node = Node(key)
        self._dll.add(node)
        self._dict[key] = node
        super().__setitem__(key, value)

        if len(self) > self.maxsize:
            node = self._dll.tail
            self._dll.remove(node)
            key = node.data
            self._dict.pop(key)
            super().pop(key)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        node = self._dict[key]
        self._dll.remove(node)
        self._dll.add(node)
        return value

    def __delitem__(self, key):
        raise NotImplementedError

    def pop(self, key):
        raise NotImplementedError

    def __iter__(self):
        """Iterate through list in order."""
        node = self._dll.head
        while node is not self._dll.terminal:
            yield node
            node = node.prev
