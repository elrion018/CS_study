#######################
#이것은 백준15686번 치킨배달 문제를 푼 코드입니다. 조합을 통한 모든 경우의 수들을 검사했습니다.
#programmer : 천재민
#programming date : 2019-03-28
#######################
ans = 10e9
#메인 메소드(조합, 경우의 수, 최단 치킨거리)
def cal(idx, cnt):
    global ans #정답 변수 글로벌 변수 설정
    if idx > len(chicken):
        return

    if cnt == M: #치킨거리 구하기.
        s = 0 #도시의 치킨거리
        for i in home:
            hx, hy = i
            d = 10e9
            for j in c:
                cx, cy = chicken[j]
                d = min(d, abs(cx-hx) + abs(cy-hy))
            s += d
        ans = min(ans, s)
        return
    c.append(idx)
    cal(idx+1, cnt+1)
    c.pop()
    cal(idx+1, cnt)

    

#N*N 도시맵 입력받기 M폐업하지 않을가게 입력받기
N, M = list(map(int, input().split()))
map_ = [list(map(int, input().split())) for _ in range(N)]
#정답 변수 선언
ans = 10e9
#home리스트, chicken리스트 선언
home, chicken, c  = [], [], [] 
#home, chicken에 좌표정보 넣기
for i in range(N*N):
    a = (int) (i / N)
    b = (int) (i % N)
    if map_[a][b] == 1:
        home.append([a,b])
    elif map_[a][b] == 2:
        chicken.append([a,b])
cal(0,0)
print(ans)