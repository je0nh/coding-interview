def solution(arr, queries):
    answer = []
    for querie in queries:
        all = []
        for i in range(querie[0], querie[1] + 1):
            all.append(arr[i])
        all.sort()
        
        for j in range(len(all)):
            if all[-1] < querie[2] + 1:
                answer.append(-1)
                break
            elif all[j] > querie[2]:
                answer.append(all[j])
                break
                
    return answer
