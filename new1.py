def min_changes_to_mountain(N, array):
    middle = N // 2
    changes = 0

    # Check and adjust the endpoints
    changes += abs(array[0] - array[N-1])

    # Check and adjust elements around the middle
    for i in range(middle):
        if array[i] != array[N-1-i]:
            changes += abs(array[i] - array[N-1-i]) - 1

    return changes

# Input example
N = 5
array = [1, 2, 3, 4, 5]

# Call the function and print the result
print(min_changes_to_mountain(N, array))