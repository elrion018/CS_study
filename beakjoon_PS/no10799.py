# 입력
strings = list(input())

stack = []  # 막대기 담을 스택마련
prev = None  # 전의 괄호를 기억하기 위한 변수 선언
result = 0  # 최종 금속판 갯수

for present in strings:

    if prev == None:  # prev가 비어있다면 넣어주기
        prev = present
    elif prev == '(' and present == ')':  # 레이저인 경우
        if len(stack) == 0:  # 그러나 막대기 스택이 비어있는 경우
            prev = present
        else:  # 아닌 경우 레이저 카운트 추가
            stack[-1] += 1
            prev = present
    elif prev == '(' and present == '(':  # 막대기 시작인 경우
        stack.append(0)  # 스택에 막대기 추가 레이저 카운트는 0
        prev = present
    elif prev == ')' and present == '(':
        prev = present
    elif prev == ')' and present == ')':  # 막대기가 끝나는 경우
        laser_cnt = stack.pop()
        result += laser_cnt + 1  # 막대기 제거
        prev = present
        if stack:  # 막대기가 남아있는 경우 아래에 깔린 쇠막대기에 레이저 갯수 알려주기
            stack[-1] += laser_cnt

print(result)
