def bubbleUp(arr):
    swapped = True
    while swapped == True:
        swapped = False
        i = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
    print arr


y = [4,3,1,5,-10,0]
bubbleUp(y)

def bubbleDown(arr):
    swapped = True
    while swapped == True:
        swapped = False
        i = len(arr) - 1
        while i > 0:
            if arr[i] < arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
                swapped = True

            i -= 1

    print arr


x = [4,3,1,5,0,10,-4,3,9,0,-20]
bubbleDown(x)
