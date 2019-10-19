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

def mostFrequent(list):
    counter = 0
    num = list[0]

    for i in list:
        currentFrequency = list.count(i)
        if(currentFrequency > counter):
            counter = currentFrequency
            num = i
print("Mode: " + str( mostFrequent(userList)))

range1 = min(userList)
range2 = max(userList)
range = (range2 - range1)
print("Range: " + str(range))
