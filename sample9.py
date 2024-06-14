def find_house(r,unit,n,arr):
    if arr is None:
        return -1
    
    required_food=r*unit
    available_food=sum(arr)
    
    if available_food<required_food:
        return 0
    
    current_food = 0
    for i in range(n):
        current_food+=arr[i]
        if current_food>required_food:
            return i + 1   
    return -1
r = 7
unit = 2
n = 8
arr = [2, 8, 3, 5, 7, 4, 1, 3]
result = find_house(r, unit, n, arr)
print(f"Output: {result}")