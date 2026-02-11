# 테스트 케이스 입력 받기
T = int(input())

# 테스트 케이스 만큼 반복
for tc in range(1, T+1):
    # 각 테스트 케이스의 번호
    t = input().strip()

    # 학생들 점수 입력
    score = list(map(int, input().split()))

    # 1. 카운팅 배열 생성
    # 우리가 봐야할건  '학생수'가 아니라 '점수 배열'
    # 따라서 cnt 만들때 1001개 말고 101개 만들어야함
    cnt = [0] * 101 

    # score 리스트 안에 원소 s의 발생 횟수 기록
    for s in score: 
        cnt[s] += 1
    
    # 2. 카운팅 정렬로 정렬된 리스트 생성
    sorted_list = []
    for i in range(101):
        sorted_list += [i] * cnt[i]
    
    # 3. 최빈수 찾기
    max_count = 0
    answer = 0

    # 0~100까지 탐색
    for i in range(101):
        # 더 큰 빈도 나오면 갱신
        if cnt[i] > max_count:
            max_count = cnt[i]
            answer = i
        # 빈도가 같으면 더 큰 점수로 계산
        elif cnt[i] == max_count:
            if i > answer:
                answer = i

    print(f"#{t} {answer}")
