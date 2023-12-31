def solution(n):
    # 1 ~ n까지의 수 포함하는 리스트 만들기
    num_list1 = [num1 for num1 in range(n+1)]
    total = 0

    # 1 ~ num1까지의 수 포함하는 리스트 만들기
    for num1 in num_list1:
        num_list2 = [num2 for num2 in range(num1+1)]
        count = 0
        # 반복문으로 num의 약수 갯수 카운팅
        for num2 in num_list2:
            # ZeroDivisionError 대비해서 try문 사용
            try:
                num1 % num2
                if num1 % num2 == 0:
                   count += 1  
            except:
                continue

        # 카운팅한 수가 3이상이면 합성수로 판단
        if count >= 3:
            total += 1

    return total


# 너무 깔끔한 답변, 컴파일 시간까지 고려한 답변
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

print(solution(10))
print(solution(15))