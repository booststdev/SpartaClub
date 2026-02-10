# T : 테스트 케이스 개수
T = int(input()) 

for t in range(1, T+1):

    # 각 테스트 케이스에서 주어지는 숫자
    num = list(map(int, input().split())) 

    # sum : num 리스트 안에 있는 원소들 합
    sum = 0

    # len : num 리스트 길이
    len = 0 
    
    # sum, len 구하기
    # num 리스트 안에 있는 원소를 i라고 지정
    for i in num: 
        # num안에 i가 있으면
        if i in num:
            len += 1 # len에 1 더하기
            sum += i # sum에 i 더하기
    
    # num 리스트에 있는 원소들의 평균값을 반올림 해서
    # result에 저장
    result = round(sum / len)

    # 결과 출력
    print(f"#{t} {result}")


