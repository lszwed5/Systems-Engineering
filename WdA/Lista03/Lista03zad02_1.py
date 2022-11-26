import Lista03zad01
import copy


queue = Lista03zad01.Queue()
queue.generate_queue(30)

office1 = Lista03zad01.Office(["A", "A", "A", "B", "B", "B", "C", "C", "C"], 0)
office2 = Lista03zad01.Office(["A", "A", "B", "B", "C", "C", "E", "E", "E"], 0)
office3 = Lista03zad01.Office(["A", "B", "B", "C", "C", "C", "E"], 0)


office1.queue.head = copy.deepcopy(queue.head)
print("\n----------------------------------------------- Office 1 -----------------------------------------------")
office1.mainloop()
office1.info()
print()

office2.queue.head = copy.deepcopy(queue.head)
print("\n----------------------------------------------- Office 2 -----------------------------------------------")
office2.mainloop()
office2.info()
print()

office3.queue.head = copy.deepcopy(queue.head)
print("\n----------------------------------------------- Office 3 -----------------------------------------------")
office3.mainloop()
office3.info()
print()
