# 17 - Binary Search

> This README was written by an AI assistant (Claude) based on the existing `Solution.py`.

## Problem Description

Given an array of integers `nums` sorted in ascending order and an integer `target`, return the index of `target` in `nums`. If `target` does not exist, return `-1`. The algorithm must run in O(log n) time.

## Approach

Classic **iterative binary search**. Because the array is sorted, comparing `target` with the middle element tells us which half can still contain it, so each step discards half of the remaining search range.

The solution keeps two pointers, `left` and `right`, that bound the inclusive range still to be searched.

## Step-by-Step Logic

1. Set `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`:
   1. Compute `mid = left + (right - left) // 2`. This equals `(left + right) // 2` but avoids integer overflow in languages with fixed-width integers.
   2. If `nums[mid] == target`, return `mid`.
   3. If `nums[mid] < target`, the target can only be on the right, so set `left = mid + 1`.
   4. Otherwise `nums[mid] > target`, so the target can only be on the left. Set `right = mid - 1`.
3. If the loop ends, the range is empty and the target is absent, so return `-1`.

## Example Walkthrough

Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`

| left | right | mid | nums[mid] | decision |
|------|-------|-----|-----------|----------|
| 0 | 5 | 2 | 3 | 3 < 9, so `left = 3` |
| 3 | 5 | 4 | 9 | match, return `4` |

Output: `4`

Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2`

| left | right | mid | nums[mid] | decision |
|------|-------|-----|-----------|----------|
| 0 | 5 | 2 | 3 | 3 > 2, so `right = 1` |
| 0 | 1 | 0 | -1 | -1 < 2, so `left = 1` |
| 1 | 1 | 1 | 0 | 0 < 2, so `left = 2` |

Now `left > right`, so the output is `-1`.

## Complexity

- **Time:** O(log n). The search range halves on every iteration.
- **Space:** O(1). Only a few integer variables are used.
