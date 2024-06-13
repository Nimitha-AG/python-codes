def is_element_present(arr, element):
    return element in arr
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
element = int(input("Enter the element to search: "))
if is_element_present(arr, element):
    print(f"{element} is present in the array.")
else:
    print(f"{element} is not present in the array.")
