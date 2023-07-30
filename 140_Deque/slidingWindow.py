from collections import deque

def max_in_sliding_window(nums, k):
    result = []
    dq = deque()
    for i, num in enumerate(nums):
        while dq and num >= nums[dq[-1]]:
            print("dq",dq[-1])
            print()
            dq.pop()
        dq.append(i)
        print(i,num,dq)
        if i - dq[0] >= k:
            dq.popleft()
            print("dq popleft: ",dq)
        if i >= k - 1:
            result.append(nums[dq[0]])
            print("res: ",result)
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_in_sliding_window(nums, k))

"""
The first window is [1, 3, -1], and the maximum value in this window is 3.
The second window is [3, -1, -3], and the maximum value in this window is 3.
The third window is [-1, -3, 5], and the maximum value in this window is 5.
The fourth window is [-3, 5, 3], and the maximum value in this window is 5.
The fifth window is [5, 3, 6], and the maximum value in this window is 6.
The sixth window is [3, 6, 7], and the maximum value in this window is 7.
So, the output is [3, 3, 5, 5, 6, 7].

"""
