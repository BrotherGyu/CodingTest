"""
04. 가장 흔한 단어
    Page: 151
    - Input / Output
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
    / "ball"

    - 실행시간
    *
"""
from time_measure import measure_execution_time

import re
import collections

def solution(paragraph, banned) -> str:
    paragraph = re.sub('[^\w\s]', '', paragraph.lower()).split(' ')
    answer = collections.Counter(paragraph)
    answer.pop(banned[0])
    return answer.most_common(1)[0][0]

if __name__ == "__main__":
    # 첫 번째 테스트 케이스
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    result1, time1 = measure_execution_time(solution, paragraph, banned)
    print(f"Output: {result1}, Execution Time: {time1:.3f} ms")