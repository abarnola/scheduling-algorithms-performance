import random
from sjf_np import sjf
from round_robin import rr
from fcfs import fcfs

bt = []
at = []
ids = []
wt = []

def generateProcesses(n):
    for i in range(n):
        ids.append(i + 1)
        at.append(i+1)
        bt.append(random.randint(5, 15))

def clearProcesses():
    global bt, at, ids, wt
    bt = []
    at = []
    ids = []
    wt = []

x = int(input('times to run algorithms: '))
for i in range(x):
    n = random.randint(5, 100)
    print('n = ' + str(n))
    generateProcesses(n)
    fcfs(n, ids, bt, at)
    #print(bt)
    rr(n, ids, bt, 2)
    # Need to fix sjf
    sjf(n, ids, bt, at)
    clearProcesses()
