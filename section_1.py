def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr




def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



def linear_search(arr, target):
   
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    
    arr = [20, 25, 12, 22, -11,11,0,-22]
    print("Original Array:", arr)

    sorted_arr = selection_sort(arr.copy())
    print("Selection Sort:", sorted_arr)

    sorted_arr = bubble_sort(arr.copy())
    print("Bubble Sort:", sorted_arr)

    target = 0

    index = linear_search(arr, target)
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the array.")

   
