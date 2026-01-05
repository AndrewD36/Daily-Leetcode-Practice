# Arrays:

## Sliding Window (Fixed Size)
This algorithm maintains 2 pointers that are of length k apart from eachother and fit a fixed constraint.

The brute force approach is to consider every subarray of size k and check if there are duplicates as so:

```python
def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False
```

With array [1,2,3,2,3,3] and k = 3

The approach becomes an O(n^2) solution because the outer loop will loop n times and the inner loop repeats k times where k <= n.

## Sliding Window (Variable Size)

## Two Pointers

