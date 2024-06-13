def findTriplets(arr, n):
    arr.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == 0:
                return 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return 0
n1 = 5
arr1 = [0, -1, 2, -3, 1]
print(findTriplets(arr1, n1))  
n2 = 3
arr2 = [1, 2, 3]
print(findTriplets(arr2, n2))