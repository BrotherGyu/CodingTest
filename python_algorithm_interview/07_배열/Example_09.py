"""
09. 세수의 합
    Page: 184
    - Input / Output
    Input: nums - [-1, 0, 1, 2, -1, -4]
    Output: [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    
    - https://leetcode.com/problems/3sum/
    - 실행시간
    *
"""

from typing import List
from time_measure import measure_execution_time

class Solution:
    def threeSum(self, nums: List[int]) -> int:
        result = []
        nums.sort()
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1

            while left < right:
                sum_value = nums[idx] + nums[left] + nums[right]
                if sum_value == 0:
                    result.append([nums[idx], nums[left], nums[right]])
                    left, right = self.duplicate_check(nums, left, right)

                elif sum_value < 0:
                    left += 1
                else:
                    right -= 1        
        return result
    
    def duplicate_check(self, nums, left, right):
        while left < right and nums[left] == nums[left + 1]:
            left += 1
        while left < right and nums[right] == nums[right - 1]:
            right -= 1
        return left+1, right-1
    


if __name__ == "__main__":
    solution = Solution()
    # 첫 번째 테스트 케이스
    nums = [-1, 0, 1, 2, -1, -4]
    result1, time1 = measure_execution_time(solution.threeSum, nums)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")