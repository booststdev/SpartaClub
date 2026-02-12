# T : 테스트 케이스 개수
T = int(input())

for tc in range(1, T + 1):
    # N : 주어진 수
    N = int(input())

    # primes : 분해할 소수 리스트
    primes = [2, 3, 5, 7, 11]

    # exponents : 각 소수의 지수를 담을 리스트
    exponents = []

    # 각 소수에 대해 지수를 계산
    for p in primes:
        count = 0           # 현재 소수의 지수 초기화
        while N % p == 0:   # N이 p로 나누어 떨어지면
            N //= p         # N을 p로 나누고
            count += 1      # 지수 1 증가
        exponents.append(count)  # 리스트에 지수 추가

    # answer : 출력할 문자열로 변환
    answer = ' '.join(map(str, exponents))

    # 결과 출력 (예: #1 2 1 1 0 0)
    print(f"#{tc} {answer}")
