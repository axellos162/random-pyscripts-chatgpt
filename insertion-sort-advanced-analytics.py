#  implementation of the insertion sort function that calculates the number of shifts required to sort the array:

def insertionSort(arr):
    shifts = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        
        arr[j + 1] = key
    
    return shifts


# the main function that takes the input and calls the insertionSort function for each query:
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        shifts = insertionSort(arr)

        print(shifts)
