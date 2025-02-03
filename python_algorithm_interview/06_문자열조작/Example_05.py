"""
05. 그룹 애너그램
    Page: 153
    - Input / Output
    ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    /
    [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]
    - https://leetcode.com/problems/group-anagrams/
    - 실행시간
    *
"""
from time_measure import measure_execution_time

from collections import defaultdict

def solution(input_data) -> list:
    answer_dict = defaultdict(list)
    for value in input_data:
        answer_dict[''.join(sorted(value))].append(value)
    return list(answer_dict.values())

if __name__ == "__main__":
    # 첫 번째 테스트 케이스
    input_data = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    result1, time1 = measure_execution_time(solution, input_data)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")