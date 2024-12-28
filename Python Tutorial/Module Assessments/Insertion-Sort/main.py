def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be placed in the correct position
        j = i - 1

        # Shift elements of the sorted part to the right to make space for the key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at its correct position
        arr[j + 1] = key

def main():
# Example usage
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)

    insertion_sort(arr)
    print("Sorted array:", arr)
    
if __name__ == "__main__":
    main()