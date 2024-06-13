n=int(input("enter the value of n:"))
arr=int(input("enter the array elemnets:"))
for i in range(n):
    if(1<=n<=10^6 and 1<=arr[i]<=10^6):
        total_sum=n*(n+1)/2
        array_sum=sum(arr)
        missing_number=total_sum-array_sum
        print(f"The missing number is: {missing_number}")
    else:
        exit()