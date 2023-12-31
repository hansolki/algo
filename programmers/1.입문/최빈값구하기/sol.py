def solution(array):
    # 1000까지의 범위가 0으로 채워진 리스트 만들기 
    numbers = [0 for i in range(1000)]

    # array 숫자에 해당하는 인덱스에 +1 해주기 
    for num in array:
        numbers[num] += 1

    count = 0
    # numbers에서 최빈값에 해당하는 숫자 count
    for num in numbers:
        if num == max(numbers):
            count += 1
    # count한 값이 2 이상이면 -1 반환
    if count >= 2:
        return -1
    # count한 값이 하나이면 그 값의 인덱스 반환
    else:
        return numbers.index(max(numbers))

# 딕셔너리 이용
def solution(array):
    a = []
    for i in array:
        a.append(array.count(i))    #1    1    3    3    3    1


    di = {key: value for key, value in zip(array, a)}   # 1:1, 2:1, 3:3, 4:1


    max_count = max(di.values())       # 3

    if list(di.values()).count(max_count) > 1:  #value 가 3ㅇ인 값을 count// 여러개면 -1 return
        return -1

    answer = [key for key, value in di.items() if value == max_count][0]
    
    return answer

print(solution([1,2,3,3,3,4]))
print(solution([1,1,2,2]))
print(solution([1]))