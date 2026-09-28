class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []

        result = []
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                b = nums[j]

                min_sum = a + b + nums[j+1] + nums[j+2]
                if min_sum > target:
                    break

                max_sum = a + b + nums[n-1] + nums[n-2]
                if max_sum < target:
                    continue

                pointer_1, pointer_2 = j + 1, n - 1

                while pointer_1 < pointer_2:
                    total = a + b + nums[pointer_1] + nums[pointer_2]

                    if total == target:
                        result.append([
                            a, b, nums[pointer_1], nums[pointer_2]
                        ])

                        pointer_1 += 1
                        pointer_2 -= 1

                        while (pointer_1 < pointer_2 and
                               nums[pointer_1] == nums[pointer_1 - 1]):
                            pointer_1 += 1

                        while (pointer_1 < pointer_2 and
                               nums[pointer_2] == nums[pointer_2 + 1]):
                            pointer_2 -= 1

                    elif total > target:
                        pointer_2 -= 1

                    else:
                        pointer_1 += 1

        return result
