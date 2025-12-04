def binary_search_upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value >= target:
            upper_bound = mid_value
            right = mid - 1
        else:
            left = mid + 1

    return (iterations, upper_bound)

