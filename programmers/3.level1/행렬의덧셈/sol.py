def solution(arr1, arr2):
    # 런타임 에러
    # answer = [[],[]]
    # for i in range(len(arr1)):
    #     for j in range(len(arr1[i])):
    #         answer[i].append(arr1[i][j]+arr2[i][j]) 
    # return answer

    # ? 
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j])
        
    return answer
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))