# T : 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # m : 메모리의 원래 값
    m = input().strip()

    # count : 최소 수정 횟수
    count = 0

    # prev : 이전 bit 상태
    prev = '0'

    for bit in m:
        if bit != prev:
            count += 1
            prev = bit

    print(f'#{tc} {count}')