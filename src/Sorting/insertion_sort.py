def insertion_sort(arr:list, reverse=False):
    n = len(arr)
    if n <= 1:
        return

    if reverse:
        for i in range(n):
            index = i
            for j in range(i+1, n):
                if arr[index] <= arr[j]:
                    index = j # record the max
            tmp = arr[i]
            arr[i] = arr[index]
            arr[index] = tmp
    else:
        for i in range(n):
            index = i
            for j in range(i+1, n):
                if arr[index] > arr[j]:
                    index = j
            tmp = arr[i]
            arr[i] = arr[index]
            arr[index] = tmp



