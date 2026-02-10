# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 번호를 1부터 T까지 반복
for t in range(1, T + 1):

    # N, M 입력 (두 수열의 길이)
    N, M = map(int, input().split())

    # 수열 A 입력
    A = list(map(int, input().split()))

    # 수열 B 입력
    B = list(map(int, input().split()))

    # 최댓값을 저장할 변수
    max_value = -10**9  # 매우 작은 값으로 초기화

    # 항상 A가 더 짧은 수열이 되도록 처리
    if N > M:
        # N이 M보다 크면 A와 B를 서로 바꾼다
        A, B = B, A
        N, M = M, N

    # B 위에서 A를 이동시키며 계산
    # 이동 가능한 횟수는 (긴 수열 길이 - 짧은 수열 길이 + 1)
    for i in range(M - N + 1):

        # 현재 위치에서의 곱의 합
        total = 0

        # A의 길이만큼 반복
        for j in range(N):
            # A[j]와 B[i + j]를 곱해서 total에 더함
            total += A[j] * B[i + j]

        # 현재 계산한 값이 최대값보다 크면 갱신
        if total > max_value:
            max_value = total

    # 결과 출력 형식에 맞게 출력
    print(f"#{t} {max_value}")
