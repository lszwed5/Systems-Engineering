from Robots import Robot


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class FleetStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, robot):
        node = Node(robot)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("The Stack is empty")
        else:
            removed = self.head
            self.head = self.head.next
            self.size -= 1
            removed.data.show_info()
            return removed.data

    def clear(self):
        print("Clearing values:")
        node = self.head
        while node:
            self.pop()
            node = node.next
        print("The Stack is now empty")

    def print_stack(self):
        """Prints out all the nodes in a stack to the console.
        Written in debugging purposes"""
        if self.is_empty():
            print("The Stack is empty")
        else:
            node = self.head
            while node:
                node.data.show_info()
                node = node.next


if __name__ == '__main__':
    fleet = FleetStack()
    fleet.push(Robot("AUV", 21.37, 66, True, name='1'))
    fleet.push(Robot("AUV", 21.37, 66, True, name='2'))
    fleet.push(Robot("AUV", 21.37, 66, True, name='3'))
    fleet.print_stack()
    print("\nPopped")
    fleet.pop()
    print()
    fleet.clear()
    print()
    fleet.print_stack()
