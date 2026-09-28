# LeetCode-Question-Number-16
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

# This is the result of the Solution

<img width="1917" height="907" alt="image" src="https://github.com/user-attachments/assets/8955ef6c-1338-4fe8-89b7-52ecdd60aa7b" />

# Work Flow
1. Handle the Base Case: If the array contains fewer than four elements, return an empty list because a quadruplet cannot be formed.

2. Sort the Array: Sort the array in ascending order to make it easier to use two pointers and eliminate duplicate quadruplets.

3. Fix the First Two Elements: Use two nested loops to select the first two elements (`a` and `b`). Skip duplicate elements to avoid generating repeated quadruplets.

4. Apply Pruning: Calculate the minimum and maximum possible sums for the current pair. If the minimum exceeds the target, break the inner loop. If the maximum is smaller than the target, skip the current pair.

5. Use Two Pointers: Set the left pointer to `j + 1` and the right pointer to the last index. Calculate the sum of all four elements. If the sum equals the target, add the quadruplet to the result and move both pointers. If the sum is greater, move the right pointer left; otherwise, move the left pointer right. Skip duplicate values after finding a valid quadruplet.

6. Return the Result: Continue until all possible combinations have been checked, then return the list of unique quadruplets.
