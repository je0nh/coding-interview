### 1
def solution(arr, queries):
    answer = []

    # list에 있는 내용을 하나씩 가져 올수 있다!
    for s, e, k in queries:
        tmp = []


        for x in arr[s:e+1]:
            if x > k:
                tmp.append(x)
        answer.append(-1 if not tmp else min(tmp))
    return answer

### 2
# sys 이용해서 max 숫자 지정
import sys

def solution(arr, queries):
    res = []
    for query in queries:
        s, e, k = query
        curr_min = sys.maxsize

        for i in range(s, e + 1):
            if arr[i] > k:
                curr_min = min(arr[i], curr_min)
        if curr_min == sys.maxsize:
            res.append(-1)
        else:
            res.append(curr_min)

    return res

### 3
# 제일 짧은 풀이
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        l = [i for i in arr[s:e+1] if i > k]
        answer.append(-1 if len(l) == 0 else min(l))
    return answer
