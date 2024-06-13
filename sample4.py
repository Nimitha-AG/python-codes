def find_second_largest(arr):
   
        if len(arr)< 2:
            return None 
        arr_sorted = sorted(arr)
        largest = arr_sorted[-1]
        for i in range(len(arr_sorted) - 2, -1, -1):
            if arr_sorted[i] < largest:
                return arr_sorted[i]
            return None
        else:
            exit()
n=10000
arr = [12,35,1,10,34,1]
if 2<=n<=100000  :
    second_largest = find_second_largest(arr)
    print("Sorted array:", sorted(arr))
    print("output:", second_largest)
