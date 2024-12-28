def merge_sort(arr):
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Compare elements from both halves and merge them in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
def main():

    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)

    merge_sort(arr)
    print("Sorted array:", arr)
    

if __name__ == "__main__":
    main()