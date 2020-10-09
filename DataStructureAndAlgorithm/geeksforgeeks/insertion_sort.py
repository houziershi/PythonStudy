# Python Program implementation
# of binary insertion sort

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = binary_search(arr, temp, 0, i) + 1
        for k in range(i, pos, -1):
            arr[k] = arr[k - 1]
        arr[pos] = temp


def binary_search(arr, key, start, end):
    # key
    if end - start <= 1:
        if key < arr[start]:
            return start - 1
        else:
            return start
    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid)
    else:
        return mid


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    for i in range(len(arr)):
        print("% d" % arr[i])

    # Code contributed by Mohit Gupta_OMG
