import random


class Node:
    """Class representing a single linked list node"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Claimant:
    """Class representing a single claimant"""

    def __init__(self, type_, complexity):
        self.type_ = type_
        self.complexity = complexity


class Queue:
    """Class representing a queue of claimants, structured as a single linked list"""

    def __init__(self, head=None):
        self.head = head

    def generate_queue(self, length):
        """Generates a queue of claimants of the given length with cases randomly chosen between A, B and C
        with adequate complexities"""
        for _ in range(length):
            type_ = random.choice(["A", "B", "C"])
            self.prepend(Claimant(type_, self.complexity_choice(type_)))

    def complexity_choice(self, type_):
        """Depending on the given type of case, returns a randomized corresponding complexity"""
        match type_:
            case "A":
                return random.randint(1, 4)
            case "B":
                return random.randint(5, 8)
            case "C":
                return random.randint(9, 12)

    def prepend(self, data):
        """Adds a node at the beginning of the linked list. Written only for practice purposes"""
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        """Adds a node at the end (tail) of the linked list.
        Written to be used in the early draft of the delete function"""
        node_ = Node(data)
        node = self.head
        head = self.head
        last = None
        while node:
            last = node
            node = node.next
        if last is None:
            self.head = node_
        else:
            last.next = node_
            self.head = head

    def delete(self, node):
        """Deletes the given node from a linked list by linking its preceding node to its following node"""
        current = self.head
        prev = None
        found = False
        while current and found is False:
            if current.data.type_ == node.data.type_ and current.data.complexity == node.data.complexity:
                found = True
            else:
                prev = current
                current = current.next
        if current is None:
            print("Such element does not appear in this list")
        elif prev is None:
            self.head = current.next
        else:
            prev.next = current.next


    def insertion_sort(self, order="asc"):
        """Sorts the Queue object by complexity values using insertion sort. 
        Takes in the order attribute - for an ascending sort type "asc", for a descending sort type "desc" """
        node = self.head
        head1 = node
        head2 = None
        while head1:
            node = head1
            head1 = head1.next
            node.next = None
            before = None
            after = head2
            while after:
                if order == "asc":
                    if after.data.complexity > node.data.complexity:
                        break
                if order == "desc":
                    if after.data.complexity < node.data.complexity:
                        break
                before = after
                after = after.next
            if before is None:
                head2 = node
            else:
                before.next = node
            node.next = after
        self.head = head2

    def print_list(self):
        """Prints out all the nodes in a linked list to the console. Written in debugging purposes"""
        node = self.head
        while node:
            print(node.data.type_, node.data.complexity)
            node = node.next


class Counter:
    """Class representing a single counter"""

    def __init__(self, index, type_):
        self.index = index
        self.type = type_
        self.occupied_for = 0
        self.number_of_claimants = 0


class Office:
    """Class representing the whole office"""

    def __init__(self, types, queue_length):
        self.keep_running = False
        self.queue = Queue()
        self.queue.generate_queue(queue_length)
        self.iterations = 0
        self.counters = []
        self.types = types
        for i in range(len(self.types)):
            self.counters.append(Counter(i + 1, self.types[i]))

    def mainloop(self):
        """Main loop of the whole program. Assigns claimants to proper counters, counts iterations,
        deletes assigned claimants from the queue. Basically runs the whole office"""
        self.is_finished()
        while self.keep_running:
            for i in range(len(self.counters)):
                if self.counters[i].occupied_for > 0:
                    self.counters[i].occupied_for -= 1
                else:
                    new_claimant = self.find_claimant(self.counters[i].type)
                    if new_claimant:
                        self.counters[i].occupied_for = new_claimant.data.complexity
                        self.counters[i].number_of_claimants += 1
                if __name__ == '__main__':
                    print(f"C {self.counters[i].index} comp {self.counters[i].occupied_for}", end="\t")
            if __name__ == '__main__':
                print()
            self.iterations += 1
            self.is_finished()

    def info(self):
        """Prints out number of serviced claimants for every counter alone, the number of all the serviced clients
        and number of iterations needed for all the claimants to be serviced.
        Meant to be used AFTER the mainloop method"""
        serviced = 0
        print("\n---------------------------- Each Counter ----------------------------")
        for counter in self.counters:
            print(f"\tCounter {counter.index} of type {counter.type} serviced {counter.number_of_claimants} claimants")
            serviced += counter.number_of_claimants
        print("\n----------------------------- Altogether -----------------------------")
        print(f"\tNumber of claimants serviced: {serviced}")
        print("\n----------------------------- Iterations -----------------------------")
        print(f"\tNumber of iterations until all claimants have been serviced: {self.iterations}")

    def is_finished(self):
        """Checks if there are any claimants left to be serviced (including those already by the counters)"""
        self.keep_running = False
        for counter in self.counters:
            if counter.occupied_for or self.queue.head:
                self.keep_running = True

    def find_claimant(self, counter_type):
        """Returns the linked list's first node matching the one given, concurrently deleting it from the list.
        The whole process might be considered an extraction of the sought node"""
        node = self.queue.head
        while node:
            if counter_type == "E":
                self.queue.delete(node)
                return node
            else:
                if counter_type == node.data.type_:
                    self.queue.delete(node)
                    return node
                else:
                    node = node.next
        if node is None:
            # print(f"There are no more claimants with the {counter_type} type case")
            return None


if __name__ == "__main__":
    office = Office(["A", "A", "A", "B", "B", "B", "C", "C", "C", "E"], 40)
    # office.queue.print_list()
    office.mainloop()
    office.info()

# Close counters for which there are no more claimants waiting
# Divide the main queue into three smaller queues, each one for a different type
