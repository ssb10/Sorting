def partition(input_array,low,high):
    pivot=input_array[high]

    i=low - 1

    for j in range(low,high):
        if input_array[j]<=pivot:
            i=i+1
            temp=input_array[i]
            input_array[i]=input_array[j]
            input_array[j]=temp

    temp=input_array[i+1]
    input_array[i+1]=input_array[high]
    input_array[high]=temp

    return (i+1)

def quicksort(input_array,low,high):
    if low<high:
        p = partition(input_array,low,high)

        quicksort(input_array,low,p-1)
        quicksort(input_array,p+1,high)

print("--Quick Sort--")
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

quicksort(input_array,0,int(n)-1)

print("The sorted array is:")
print(input_array)