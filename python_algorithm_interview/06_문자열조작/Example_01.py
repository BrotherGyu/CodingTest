"""
01. 유효한 팰린드롬
    Page: 138
    - Input / Output-
    "A man, a plan, a canal: Panama" / true
    "race a car" / false
"""

import collections
from time_measure import measure_execution_time

def solution(input_data) -> bool:
    strs = collections.deque(input_data.lower())
    while len(strs) > 1:
        if not strs[0].isalnum():
            strs.popleft()
            continue

        if not strs[-1].isalnum():
            strs.pop()
            continue

        if strs[0] != strs[-1]:
            return False
        strs.popleft()
        strs.pop()
    return True

if __name__ == "__main__":
    # 첫 번째 테스트 케이스
    result1, time1 = measure_execution_time(solution, "A man, a plan, a canal: Panama")
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    # 두 번째 테스트 케이스
    result2, time2 = measure_execution_time(solution, "race a car")
    print(f"Output: {result2}, Execution Time: {time2:.3f} ms")