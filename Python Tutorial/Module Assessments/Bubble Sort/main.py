import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
        
    random_list = [random.randint(1, 100) for _ in range(10)]  # Generates a list of 10 random numbers between 1 and 100
    print("Original list:", random_list)
    
    bubble_sort(random_list)
    print("Sorted list:", random_list)

if __name__ == "__main__":
    main()