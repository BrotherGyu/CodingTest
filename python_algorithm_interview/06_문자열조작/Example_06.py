"""
05. 그룹 애너그램
    Page: 153
    - Input / Output
    Input: s = "babad"
    Output: "bab"

    Input: s = "cbbd"
    Output: "bb"

    - https://leetcode.com/problems/longest-palindromic-substring/
    - 실행시간
    *
"""
from time_measure import measure_execution_time


def solution(s: str) -> str:
    if len(s) <= 2:
        if s[0]==s[-1]:
            return s
        return s[0]

    result = ""
    for i in range(len(s) - 1):
        result = max(result, search(s, i, i+1), search(s, i, i+2), key=len)
    return result

def search(str_value:str, left: int, right: int) -> str:
        while left >= 0 and right <len(str_value) and str_value[left] == str_value[right]:
            left -= 1
            right += 1
        return str_value[left + 1 : right]

if __name__ == "__main__":
    # 첫 번째 테스트 케이스
    input_data = "babad"
    result1, time1 = measure_execution_time(solution, input_data)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    input_data = "cbbd"
    result1, time1 = measure_execution_time(solution, input_data)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    input_data = "a"
    result1, time1 = measure_execution_time(solution, input_data)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    input_data = "aa"
    result1, time1 = measure_execution_time(solution, input_data)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    input_data = "abc"
    result1, time1 = measure_execution_time(solution, input_data)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    input_data = "aba"
    result1, time1 = measure_execution_time(solution, input_data)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")