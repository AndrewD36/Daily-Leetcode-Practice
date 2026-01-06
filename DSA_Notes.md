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

The approach becomes a O(n^2) or O(n * k) solution because the outer loop will loop n times and the inner loop repeats k times where k <= n.

Using a hashset can optimize this sliding window algorithm in this exact example. The hashset will detect duplicates already meaning we don't have to manually compare the two pointers values in each window.

```python
def closeDuplicates(nums, k):
    window = set() # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False
```

## Sliding Window (Variable Size)

## Two Pointers

The main idea is to have a left pointer **L** and right pointer **R** that start at some indices of an array. They move throughout the array to compare values at specific indices.