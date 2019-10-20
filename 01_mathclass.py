userListCount = int(input("Enter number of elements: "))
userList = list(map(int,input("\nEnter the numbers: ").strip().split()))
userListLen = len(userList)

getSum = sum(userList)
mean = getSum / userListLen
print("Mean: " + str(mean))

userList.sort()
if userListLen % 2 == 0:
    median1 = userList[userListLen//2]
    median2 = userList[userListLen//2]
    median = (median1 + median2) / 2
else:
    median = userList[userListLen//2]
print("Median: " + str(median))

from collections import Counter

data = Counter(userList)
getMode = dict(data)
mode = [k for k, v in getMode.items() if v == max(list(data.values()))]
if len(getMode) == userListLen:
    getMode = "None"
else:
    getMode = "Mode: " + ", ".join(map(str, mode))
print(getMode)

range1 = min(userList)
range2 = max(userList)
range = (range2 - range1)
print("Range: " + str(range))
