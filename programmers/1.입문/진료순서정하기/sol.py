def solution(emergency):
    # emergency의 길이만큼 0으로 채워진 리스트 만들기
    answer = [0 for num in range(len(emergency))] 
    # emergency를 역순정렬한 리스트 만들기
    my_list = sorted(emergency, reverse=True)
    # my_list에서 순위 구해서 answer의 num인덱스에 넣기
    for num in emergency:
        answer[emergency.index(num)] = my_list.index(num) + 1

    return answer

# dictionary 이용한 문제 풀이 
def solution(emergency):
    dict1={}
    list1=sorted(emergency,reverse=True)
    for i,x in enumerate(list1,start=1):
        dict1[x]=i
    answer=[dict1[x] for x in emergency]
    return answer

print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))