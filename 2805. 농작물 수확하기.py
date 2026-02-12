# T : 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 농장 크기 입력받기
    N = int(input())

    # farm : N x N 농장 정보 입력 (2차원 리스트)
    farm = [list(map(int, input().split())) for _ in range(N)]

    # total : 마름모 영역 원소의 합
    total = 0
    
    # center : 농장의 중앙 인덱스
    # 예) N=5 → center = 2
    center = N // 2

    # center와의 거리만큼 좌우 범위 결정 (마름모 형태)
    # i 인덱스 : 행 기준 -> 세로(위 -> 아래)로 움직임
    for i in range(N):
        start = center-abs(center-i)
        end = center + abs(center-i)
    
    # total 구하기
    # j 인덱스 : 열 기준 -> 가로(왼쪽 -> 오른쪽)으로 움직임
    for j in range(start, end+1):
        total += farm[i][j]
    
    print(f"#{tc} {total}")
