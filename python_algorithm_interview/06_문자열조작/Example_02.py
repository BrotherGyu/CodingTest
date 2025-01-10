"""
02. 문자열 뒤집기
    Page: 145
    - Input / Output-
    ["h", "e", "l", "l", "o"] / ['o', 'l', 'l', 'e', 'h']
    ["H", "a", "n", "n", "a", "h"] / ['h', 'a', 'n', 'n', 'a', 'H']

    - 실행시간
    풀이 1 - 216 ms
    풀이 2 - 208 ms
"""

from time_measure import measure_execution_time

def solution(input_data) -> list:
    # return input_data[::-1]
    input_data.reverse()
    return input_data

if __name__ == "__main__":
    # 첫 번째 테스트 케이스
    result1, time1 = measure_execution_time(solution, ["h", "e", "l", "l", "o"])
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    # 두 번째 테스트 케이스
    result2, time2 = measure_execution_time(solution, ["H", "a", "n", "n", "a", "h"])
    print(f"Output: {result2}, Execution Time: {time2:.3f} ms")