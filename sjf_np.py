import operator

# sort array a by index n
def sortByIndex(a, n):
    a.sort(key = operator.itemgetter(n))
    return a

'''
completionTime(Array[n][6], n): returns completion times

Each row in the array represents a process, where positions:
    0. pid
    1. arrival time
    2. burst time
    3. turnaround time
    4. waiting time
'''
def completionTime(arr, n):
    val = -1
    temp = -1
    arr[0][3] = arr[0][1] + arr[0][2]
    arr[0][4] = arr[0][3] - arr[0][1]
    arr[0][5] = arr[0][4] - arr[0][2]
    for i in range(1, n):
        temp = arr[i - 1][3]
        low = arr[i][2]
        for j in range(i, n):
            if (temp >= arr[j][1] and low >= arr[j][2]):
                low = arr[j][2]
                val = j
            arr[val][3] = temp + arr[val][2]
            arr[val][4] = arr[val][3] - arr[val][1]
            arr[val][5] = arr[val][4] - arr[val][2]

            for k in range(6):
                tmp = arr[val][k]
                arr[val][k] = arr[i][k]
                arr[i][k] = tmp
    return arr
processes = [
        [1, 2, 3, 0, 0, 0],
        [2, 0, 4, 0, 0, 0],
        [3, 4, 2, 0, 0, 0],
        [4, 5, 4, 0, 0, 0]
    ]

def sjf(n, ids, bt, at):
    arr = []
    for i in range(n):
        arr.append([0] * 6)
        arr[i][0] = ids[i]
        arr[i][1] = at[i]
        arr[i][2] = bt[i]
    arr = sortByIndex(arr, 2)
    completionTime(arr, n)

    total_bt = 0
    total_tat = 0
    total_wt = 0
    for i in range(n):
        total_bt += arr[i][2]
        total_tat += arr[i][4]
        total_wt += arr[i][5]
    avg_bt = round(total_bt/n, 3)
    avg_tat = round(total_tat/n, 3)
    avg_wt = round(total_wt/n, 3)

    out = open('out/sjf.csv', 'a+')
    line = ''
    line += str(n) + ', '
    line += str(avg_bt) + ', '
    line += str(avg_tat) + ', '
    line += str(avg_wt) + '\n'
    out.write(line)

if (__name__ == '__main__'):
    processes = sortByIndex(processes, 2)
    completionTime(processes, 4)
    for i in range(4):
        print(processes[i])
