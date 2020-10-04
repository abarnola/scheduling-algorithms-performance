def getWaitingTimes(n, ids, bt, wt, at):
    service_times = [0] * n
    service_times[0] = 0
    wt[0] = 0

    for i in range(1, n):
        service_times[i] = service_times[i-1] + bt[i-1]

        wt[i] = service_times[i] - at[i]

        if (wt[i] < 0): wt[i] =  0

def getTurnaroundTimes(n, ids, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findAverageTime(n, ids, bt, at):
    wt = [0] * n
    tat = [0] * n
    compl_time = [0] * n

    getWaitingTimes(n, ids, bt, wt, at)
    getTurnaroundTimes(n, ids, bt, wt, tat)

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time[i] = tat[i] + at[i]
    # Write to console
    print('Average Waiting Time: %.3f' %(total_wt/n))
    print('Average Turnaround Time: %.3f' %(total_tat/n))

    # Write to file
    out = open('out/output.fcfs.txt', 'w')
    out.write('\nAverage Waiting Time: %.3f' %(total_wt/n))
    out.write('\nAverage Turnaround Time: %.3f' %(total_tat/n))

ids = [0, 1, 2, 3, 4, 5]
at = [0, 1, 2, 3, 4, 5]
bt = [2, 5, 6, 3, 8, 2]

findAverageTime(6, ids, bt, at)

