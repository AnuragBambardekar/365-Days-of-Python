from collections import deque

def max_in_sliding_window(nums, k):
    result = []
    dq = deque()
    for i, num in enumerate(nums):
        while dq and num >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i - dq[0] >= k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_in_sliding_window(nums, k)) # Output: [3, 3, 5, 5, 6, 7]
