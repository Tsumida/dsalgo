def bubble_sort(arr:list, reverse=False):
    n = len(arr)
    if n <= 1:
        return

    if reverse:
        for i in range(n-1, -1, -1):
            for j in range(0, i):
                if arr[j] < arr[j+1]:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
            # so, arr[i] is the maximal ele in arr[0, i]
    else:
        for i in range(0, n, 1):
            for j in range(n-2, i-1, -1):
                if arr[j] > arr[j+1]:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
            # so, arr[i] holds the minimal ele in [i, n)
