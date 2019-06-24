# recursive binary search

def binarySearch (arr, l, r, x):

    if r >= l:

        mid = l + (r-l)/2

        if arr[mid] == x:
            return mid
        # if element is smaller, its only in left
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        # else the elemtnt is only in right
        else:
            return binarySearch(arr, mid+1, r, x)

            # not present
    else:
        return -1

#helper code

arr = [1,2,3,4,5]
x = 3
results = binarySearch(arr, 0, len(arr)-1, x)

if results != -1:
    print("element is at index:", results)

else:
    print("element is not present in array")


#iterative binary search

def Iterativesearch(arr2, l, r, x):
    while l <= r:
        mid = l + (r-1)/2;
        #if element is at middle
        if arr2[mid] == x:
            return mid
        # if element is greater, ignore left half
        elif arr2[mid] < x:
            l = mid + 1
        # if element is smaller, ignore right half
        else:
            r = mid - 1
    # element not present
    return -1

# helper code

arr2 = [2,3,5,6,7]
x = 3

results = Iterativesearch(arr2, 0, len(arr2)-1, x)

if results != -1:
    print("element is at index:", results)

else:
    print("element is not present in array")
