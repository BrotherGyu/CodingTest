"""
07. 두 수의 합
    Page: 173
    - Input / Output
    Input: nums = [2, 7, 11, 15], target = 9
    Output: "[0, 1]"

    - https://leetcode.com/problems/two-sum/
    - 실행시간
    *
"""
from typing import List
from time_measure import measure_execution_time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, value in enumerate(nums):
            if (target - value) in nums[idx + 1:]:
                return [idx, nums[idx + 1:].index((target - value))+ idx + 1]
    
    # leetcode
    # Runtime: 0ms
    # Beats: 100.00%
    def twoSum_dict(self, nums: List[int], target: int) -> List[int]:
        twosum_dict = dict()
        for idx, value in enumerate(nums):
            try:
                return [twosum_dict[value], idx]
            except:
                twosum_dict[target - value] = idx

    # 코딩 인터뷰에서는 명확한 코드가 더 중요하므로 if-in 방식을 사용하는 것이 더 적절
    def twoSum_optimal(self, nums: List[int], target: int) -> List[int]:
        twosum_dict = {}
        for idx, value in enumerate(nums):
            if value in twosum_dict:
                return [twosum_dict[value], idx]
            twosum_dict[target - value] = idx

if __name__ == "__main__":
    solution = Solution()
    # 첫 번째 테스트 케이스
    nums = [2, 7, 11, 15]
    target = 9
    result1, time1 = measure_execution_time(solution.twoSum, nums, target)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    # 첫 번째 테스트 케이스
    nums = [2, 7, 11, 15]
    target = 9
    result1, time1 = measure_execution_time(solution.twoSum_dict, nums, target)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    # 첫 번째 테스트 케이스
    nums = [2, 7, 11, 15]
    target = 9
    result1, time1 = measure_execution_time(solution.twoSum_optimal, nums, target)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")