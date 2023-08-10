# Sort an array using the batcher sorting

def compare_and_swap(arr, i, j):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]


def batcher_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    batcher_sort(arr[:mid])
    batcher_sort(arr[mid:])

    for step in range(n // 2):
        for i in range(step % mid, mid, 2):
            j = i + step % (mid + 1)
            k = i + step // 2 + mid
            compare_and_swap(arr, i, j)
            compare_and_swap(arr, j, k)
    return arr


def main():
    array = [5, 6, 2, 8]

    print(array)
    sorted_array = batcher_sort(array)
    print(sorted_array)


if __name__ == "__main__":
    main()
