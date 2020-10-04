def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = [0] * n  # remaining burst times

    # Copy burst time into rem_bt[]
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0 # current time

    # Traverse processes until all are not done
    while(1):
        done = True
        # Traverse all processes repeatedly
        for i in range(n):
            if (rem_bt[i] > 0):
                done = False
                if (rem_bt[i] > quantum):
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if (done == True):
            break

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findAvgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time of all processes
    findWaitingTime(processes, n, bt, wt, quantum)

    # Function to find turnaround time for all processes
    findTurnAroundTime(processes, n, bt, wt, tat)

    total_wt = 0
    total_tat = 0

    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    print('\nAverage Waiting Time: %.3f '%(total_wt/n))
    print('\nAverage Turnaround Time: %.3f' %(total_tat/n))

ids = [1, 2, 3]
n = 3
burst_time = [10, 5, 8]
quantum = 2
findAvgTime(ids, n, burst_time, quantum)
