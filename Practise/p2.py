# find 2nd largest number

def findsecondlargestarray(arr):
    """

    :return:
    """
    n = len(arr)
    arr.sort()
    for i in range(n-2, -1, -1):
        if arr[i] != arr[n - 1]:
            return arr[i]
    return -1


arr = [10,10,10]
# print(findsecondlargestarray(arr))


############ find 3rd largest number
def findthirdlargestarray(arr):
    """

    :param arr:
    :return:
    """
    n = len(arr)
    arr.sort()
    if n >= 3:
        for ii in range(n - 3, -1, -1):
            if arr[ii] != arr[n - 1] and arr[ii] != arr[n - 2]:
                return arr[ii]
    elif n < 3:
        return -1
    else:
        return arr[n]

arr = [2,2,2]
# print(findthirdlargestarray(arr))

####### array reverse
def  arrayrev(arr):
    n = len(arr)

    temp = [0]*n
    for i in range(n):
        temp[i] = arr[n-i-1]

    for i in range(n):
        arr[i] = temp[i]

arr = [1,3,4,5,7,8]
# print(arrayrev(arr))


























