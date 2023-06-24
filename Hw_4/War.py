# Define a function named greedy that takes two parameters: n (the number of tasks) and arr (a list of lists containing the start and end times of each task)
def greedy():
    # Read an integer n from the input (the number of tasks)
    n = int(input())
    # Read n lines of input, each containing two integers separated by a space (the start and end times of each task), and store them as a list of lists in arr
    arr = [[int(i) for i in input().split()] for k in range(n)]
    # Loop through each task in arr
    for i in range(len(arr)):
        # Calculate the waiting time between the current task and the previous task
        t = arr[i][0] - arr[i-1][1]
        # If the waiting time is negative, set it to zero
        t = t if t > 0 else 0
        # Append the waiting time and the actual start time (after waiting) of the current task to arr[i]
        arr[i].append(t)
        arr[i].append(arr[i][0] - t)
    # Find the index of the task with the minimum actual start time
    argument = min(range(len(arr)), key=lambda i: arr[i][3])
    # Remove that task from arr and store it in m
    m = arr.pop(argument)
    # Print the sum of the actual start time of m and the waiting times of all remaining tasks in arr
    print(m[0] + sum(a[2] for a in arr))

# Read an integer t from the input (the number of test cases)
t = int(input())
# For each test case, call the greedy function with n and arr as arguments
for _ in range(t):
    greedy()