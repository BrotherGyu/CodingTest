"""
12. 자신을 제외한 배열의 곱
    Page: 193
    - Input / Output
    Input: nums - [1,2,3,4]
    Output: [24,12,8,6]
    
    - https://leetcode.com/problems/product-of-array-except-self/
    - 실행시간
    *
"""

from typing import List
from time_measure import measure_execution_time

class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     result = []
    #     p = 1
    #     for value in nums:
    #         result.append(p)
    #         p = p * value
    #     p = 1
    #     for idx, value in enumerate(nums[::-1]):
    #         result[-idx-1] *= p
    #         p = p * value
    #     return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1
        for value in nums:
            result.append(p)
            p = p * value

        p = 1
        for idx in range(len(nums)-1, -1, -1):
            result[idx] *= p
            p *= nums[idx]
            
        return result

if __name__ == "__main__":
    solution = Solution()
    # 첫 번째 테스트 케이스
    nums = [1,2,3,4]
    result1, time1 = measure_execution_time(solution.productExceptSelf, nums)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")