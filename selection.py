def selectionSort(arr):
    for i in range(len(arr)):
        j = i + 1
        minNum = arr[i]
        swapped = False
        while j < len(arr):
            if minNum > arr[j]:
                swapped = True
                minNum = arr[j]
                idx = j
            j += 1
        if swapped:
            arr[i],arr[idx] = arr[idx],arr[i]
        i += 1
    print arr

x = [10,3,5,1,0,8,-1,30,-5,2]
selectionSort(x)


def selectionSortTwo(arr):
   for i in range(len(arr)-1,0,-1):
       idx=0
       for j in range(1,i+1):
           if arr[j]>arr[idx]:
               idx = j
       arr[i], arr[idx]= arr[idx], arr[i]
x = [10,3,5,1,0,8,-1,30,-5,2]
selectionSortTwo(x)
print(x)
