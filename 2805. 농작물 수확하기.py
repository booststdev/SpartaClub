# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]

    total1 = 0
    center = N // 2

    # 전체 행을 순회
    for i in range(N):

        # 🔹 위쪽 + 가운데 (i가 center 이하)
        if i <= center:
            start = center - i
            end = center + i

        # 🔹 아래쪽 (i가 center 초과)
        else:
            # 아래쪽은 다시 좁아져야 하므로
            # i - center 만큼 좌우에서 줄어듦
            start = i - center
            end = (N - 1) - (i - center)

        # 마름모 범위 합산
        for j in range(start, end + 1):
            total1 += int(farm[i][j])

    print(f"#{tc} {total1}")
