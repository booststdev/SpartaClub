# T : 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # N : 첫 줄에 칠할 영역의 개수
    N = int(input())

    # 10 x 10 격자 생성 (초기값 : 0)
    grid = [[0]*10 for _ in range(10)]

    # 영역 입력받고 색칠
    for _ in range(N):
        # r1, c1 : 왼쪽 위 시작 좌표 (행, 열)
        # r2, c2 : 오른쪽 아래 끝 좌표 (행, 열)
        # color  : 칠할 색 (1=빨강, 2=파랑)
        r1, c1, r2, c2, color = map(int, input().split())

        # (r1, c1) 부터 (r2, c2) 까지 색칠
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                # 아직 안 칠해진 곳
                if grid[r][c] == 0:
                    grid[r][c] = color
                # 다른 색이 이미 칠해진 경우
                elif grid[r][c] != color:
                    grid[r][c] = 3   # 보라색 처리

    # 보라색(3) 개수 세기
    purple_count = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                purple_count += 1

    print(f"#{tc} {purple_count}")
