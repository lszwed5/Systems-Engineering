import Lista03zad01
import copy
from matplotlib import pyplot as plt


office_without_E_times = []
office_without_E_asc_times = []
office_without_E_desc_times = []

office_with_E_times = []
office_with_E_asc_times = []
office_with_E_desc_times = []

for _ in range(100):
    queue = Lista03zad01.Queue()
    queue.generate_queue(40)

    office_without_E = Lista03zad01.Office(["A", "A", "A", "B", "B", "B", "C", "C", "C"], 0)
    office_with_E = Lista03zad01.Office(["A", "A", "B", "B", "C", "C", "E", "E", "E"], 0)

    office_without_E.queue.head = copy.deepcopy(queue.head)
    office_with_E.queue.head = copy.deepcopy(queue.head)

    office_without_E.mainloop()
    office_with_E.mainloop()

    office_without_E_times.append(office_without_E.iterations)
    office_with_E_times.append(office_with_E.iterations)

    office_without_E.queue.head = copy.deepcopy(queue.head)
    office_with_E.queue.head = copy.deepcopy(queue.head)
    office_without_E.iterations = 0
    office_with_E.iterations = 0
    office_without_E.queue.insertion_sort("asc")
    office_with_E.queue.insertion_sort("asc")

    office_without_E.mainloop()
    office_with_E.mainloop()

    office_without_E_asc_times.append(office_without_E.iterations)
    office_with_E_asc_times.append(office_with_E.iterations)

    office_without_E.queue.head = copy.deepcopy(queue.head)
    office_with_E.queue.head = copy.deepcopy(queue.head)
    office_without_E.iterations = 0
    office_with_E.iterations = 0
    office_without_E.queue.insertion_sort("desc")
    office_with_E.queue.insertion_sort("desc")

    office_without_E.mainloop()
    office_with_E.mainloop()

    office_without_E_desc_times.append(office_without_E.iterations)
    office_with_E_desc_times.append(office_with_E.iterations)


print("\n\nUnsorted:")
print("------------------------------------------ Average servicing time ------------------------------------------")
print(f"Office without \"E\" type counter: {sum(office_without_E_times)/len(office_without_E_times)} iterations")
print(f"Office with \"E\" type counter: {sum(office_with_E_times)/len(office_with_E_times)} iterations")

plt.figure()
bins = max([max(office_with_E_times) - min(office_with_E_times),
            max(office_without_E_times) - min(office_without_E_times)])
plt.hist(office_without_E_times, bins, stacked=True, label="3A 3B 3C", alpha=0.7, color="red")
plt.hist(office_with_E_times, bins, stacked=True, label="2A 2B 2C 3E", alpha=0.7, color="green")
plt.legend()
plt.xlabel("Time required for all the claimants to be serviced (in iterations)")
plt.ylabel("Number of queues")
plt.title("Histogram")
plt.show()


print("\n\nAscending:")
print("------------------------------------------ Average servicing time ------------------------------------------")
print(f"Office without \"E\" type counter: "
      f"{sum(office_without_E_asc_times)/len(office_without_E_asc_times)} iterations")
print(f"Office with \"E\" type counter: "
      f"{sum(office_with_E_asc_times)/len(office_with_E_asc_times)} iterations")

plt.figure()
bins = max([max(office_with_E_asc_times) - min(office_with_E_asc_times),
            max(office_without_E_asc_times) - min(office_without_E_asc_times)])
plt.hist(office_without_E_asc_times, bins, stacked=True, label="3A 3B 3C", alpha=0.7, color="red")
plt.hist(office_with_E_asc_times, bins, stacked=True, label="2A 2B 2C 3E", alpha=0.7, color="green")
plt.legend()
plt.xlabel("Time required for all the claimants to be serviced (in iterations)")
plt.ylabel("Number of queues")
plt.title("Histogram")
plt.show()


print("\n\nDescending:")
print("------------------------------------------ Average servicing time ------------------------------------------")
print(f"Office without \"E\" type counter: "
      f"{sum(office_without_E_desc_times)/len(office_without_E_desc_times)} iterations")
print(f"Office with \"E\" type counter: "
      f"{sum(office_with_E_desc_times)/len(office_with_E_desc_times)} iterations")

plt.figure()
bins = max([max(office_with_E_desc_times) - min(office_with_E_desc_times),
            max(office_without_E_desc_times) - min(office_without_E_desc_times)])
plt.hist(office_without_E_desc_times, bins, stacked=True, label="3A 3B 3C", alpha=0.7, color="red")
plt.hist(office_with_E_desc_times, bins, stacked=True, label="2A 2B 2C 3E", alpha=0.7, color="green")
plt.legend()
plt.xlabel("Time required for all the claimants to be serviced (in iterations)")
plt.ylabel("Number of queues")
plt.title("Histogram")
plt.show()

# Assigning claimants with the type which occurs most often to Counters "E"
# Servicing the most complex claimants first
# Reassigning every counter's type to "E"
# Creating more counters?
# Dividing task between counters?
