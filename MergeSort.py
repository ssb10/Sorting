def merge_sort_merge(input_array,left,mid,right):
    x1=mid-left+1
    x2=right-mid

    left_list = [0]*x1
    right_list = [0]*x2

    for i in range(0,x1):
        left_list[i]=input_array[left+i]
        i=i+1

    for i in range(0, x2):
        right_list[i] = input_array[mid+1+i]
        i=i+1


    i = 0
    j = 0
    k=left

    while i < x1 and j < x2:
        if left_list[i] < right_list[j]:
            input_array[k]=left_list[i]
            i = i + 1

        else:
            input_array[k] = right_list[j]
            j = j + 1

        k = k+1

    while i < x1:
        input_array[k]=left_list[i]
        i = i + 1
        k = k + 1

    while j < x2:
        input_array[k] = right_list[j]
        j = j + 1
        k = k + 1

def merge_sort_divide(input_array,left,right):
     if left < right:
            mid = int((left + right) / 2)

            merge_sort_divide(input_array, left, mid)
            merge_sort_divide(input_array, mid + 1, right)
            merge_sort_merge(input_array, left, mid, right)



print("--Merge Sort--")
n = input("Enter number of elements")
print(n)

input_array = []
counter = 1
while counter <= int(n):
    element = input(("Enter element " + str(counter)))
    input_array.append(int(element))
    counter = counter + 1

print("Entered array is:")
print(input_array)

merge_sort_divide(input_array, 0, int(n)-1)

print("The sorted array is:")
print(input_array)