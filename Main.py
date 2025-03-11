def max_min_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    if right == left + 1:
        if arr[left] > arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    mid = (left + right) // 2

    max_left, min_left = max_min_select(arr, left, mid)
    max_right, min_right = max_min_select(arr, mid + 1, right)

    max_value = max(max_left, max_right)
    min_value = min(min_left, min_right)
    
    return max_value, min_value

def find_max_min(arr):
    if len(arr) == 0:
        return None, None
    return max_min_select(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = [3, 15, 7, 31, 11, 4, 9, 1, 24, 2, 8, 5, 6, 12, 17, 13]
    max_val, min_val = find_max_min(arr)
    print(f"Maior valor: {max_val}")
    print(f"Menor valor: {min_val}")
