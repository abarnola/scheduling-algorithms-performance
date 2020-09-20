import random

"""
Generate a queue of processes
@param size: number of items in the queue
@param processes: number of different processes
"""
def generateQueue(size, processes):
    ids = []
    burst_times = []
    arrival_times = []
    priorities = []
    res = {}
    for i in range(size):
        ids.append(i)
        burst_times.append(random.randint(1, 15))
        arrival_times.append(i)
        priorities.append(random.randint(1, 10))

    res["ids"] = ids
    res["burst_times"] = burst_times
    res["arrival_times"] = arrival_times
    res["priorities"] = priorities

    return res

def fcfs(queue):
    ids = queue['ids']
    burst_times = queue['burst_times']
    arrival_times = queue['arrival_times']

mylist = [0]
n = 5
print(mylist * 5)
print(generateQueue(4, 4))
