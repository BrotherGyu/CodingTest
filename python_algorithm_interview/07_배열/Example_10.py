"""
10. 배열 파티션 1
    Page: 190
    - Input / Output
    Input: nums - [1,4,3,2]
    Output: 4
    
    - https://leetcode.com/problems/array-partition/
    - 실행시간
    *
"""

from typing import List
from time_measure import measure_execution_time

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

if __name__ == "__main__":
    solution = Solution()
    # 첫 번째 테스트 케이스
    nums = [1,4,3,2]
    result1, time1 = measure_execution_time(solution.arrayPairSum, nums)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")