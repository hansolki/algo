def solution(A, B):
    # 문자들 리스트화
    AA = []
    BB = []
    for char in A:
        AA.append(char)
    for char in B:
        BB.append(char)

    count = 0
    # AA와 BB를 비교하고 다르다면 맨뒤 문자 꺼내서 앞에 넣기
    # 넣고 나선 count 추가
    for i in range(len(AA)):
        if AA == BB:
            return count
        else:
            AA.insert(0, AA[-1])
            AA.pop(-1)
            count += 1 

    return -1

# 슬라이싱
def solution(A, B):
    answer = 0
    while A != B and answer < 101:

        A = ''.join([A[-1]] + list(A[:-1]))
        answer += 1

    if A != B:
        return -1

    return answer
print(solution('hello', 'ohell'))
print(solution('apple', 'elppa'))
print(solution('atat', 'tata'))
print(solution('abc', 'abc'))
