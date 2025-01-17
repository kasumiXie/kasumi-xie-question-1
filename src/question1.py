def get_change_point(arr):
    direction = None
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:  # Increasing
            if direction is None:
                direction = 'increasing'
            elif direction == 'decreasing':
                return i - 1  # point found
        elif arr[i] < arr[i - 1]:  # Decreasing
            if direction is None:
                direction = 'decreasing'
            elif direction == 'increasing':
                return i - 1  # point found
    
    return -1  # No change point



if __name__ == "__main__":
    print(get_change_point([1, 2, 4, 8, 4, 2]))