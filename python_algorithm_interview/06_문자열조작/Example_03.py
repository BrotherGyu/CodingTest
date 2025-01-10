"""
03. 로그 파일 재정렬
    Page: 148
    - Input / Output-
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    / ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

    ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    / ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

    - 실행시간
    *
"""

from time_measure import measure_execution_time

def solution(input_data) -> list:
    letter, digit, answer = [], [], []
    for value in input_data:
        if value.split()[1].isdigit():
            digit.append(value)
        else:
            letter.append(value)
    letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    answer.extend(letter)
    answer.extend(digit)
    
    return answer

if __name__ == "__main__":
    # 첫 번째 테스트 케이스
    result1, time1 = measure_execution_time(solution, ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")

    # 두 번째 테스트 케이스
    result1, time1 = measure_execution_time(solution, ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")