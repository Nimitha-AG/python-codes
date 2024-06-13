def is_element_present(arr, element):
    return element in arr

# Input array from user
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Input element to be searched
element = int(input("Enter the element to search: "))

# Check if element is present
if is_element_present(arr, element):
    print(f"{element} is present in the array.")
else:
    print(f"{element} is not present in the array.")
