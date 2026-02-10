# T : 테스트 케이스 개수
T = int(input()) 

for tc in range(1, T+1):
    # 10개의 수 입력받아서 num에 저장
    num = list(map(int, input().split()))

    # 홀수만 더해서 저장할 변수 sum 생성
    sum = 0

    # num 리스트 안에 있는 원소를 i라고 지정
    for i in num:
        if i % 2 == 1: # i가 홀수/짝수인지 판별
            sum += i # i가 홀수이면 sum에 i를 더하기
    
    #  최종 sum을 result에 저장
    result = sum
    
    # 결과 출력
    print(f"#{tc} {result}")
