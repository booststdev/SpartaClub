# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 반복
for tc in range(1, T + 1):

    # 기준 숫자 N 입력
    N = int(input())

    # 0 ~ 9 숫자를 봤는지 체크하는 리스트
    # 인덱스가 숫자를 의미 (0~9)
    seen = [0] * 10

    k = 0          # 몇 번 양을 셌는지 카운트
    total = 0      # 현재까지 본 서로 다른 숫자의 개수

    # 0~9를 모두 볼 때까지 반복
    while total < 10:

        k += 1          # 양을 한 번 더 셈
        num = N * k     # 현재 세는 양 번호

        temp = num      # 자리수 분해용 변수

        # 숫자의 각 자리 확인
        while temp > 0:

            digit = temp % 10   # 마지막 자리 숫자 추출

            # 아직 보지 않은 숫자라면
            if seen[digit] == 0:
                seen[digit] = 1   # 봤다고 표시
                total += 1        # 본 숫자 개수 증가

            temp //= 10          # 마지막 자리 제거

    # 결과 출력
    print("#" + str(tc) + " " + str(k))
