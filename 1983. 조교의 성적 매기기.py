# 테스트케이스 개수
T = int(input())

# 학점 리스트
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T + 1):
    # N : 학생 수
    # K : 알고싶은 학생의 번호
    N, K = map(int, input().split())

    # 학생 점수 리스트 생성
    students = []

    # 각 학생의 중간, 기말, 과제 점수를 입력받고 총점을 계산하여
    # students 리스트에 저장
    for i in range(N):
        # mid : 중간고사 점수
        # fin : 기말고사 점수
        # task : 과제 점수
        mid, fin, task = map(int, input().split())
        total_score = (mid * 0.35) + (fin * 0.45) + (task * 0.2)
        # (총점, 학생 번호) 튜플 형태로 저장
        students.append((total_score, i + 1)) 

    # 총점을 기준으로 내림차순 정렬
    def myf(x):
        return x[0]
    students.sort(reverse=True, key=myf)

    # 각 학생에게 학점 부여
    grade_assignment = {}
    for idx in range(N):
        grade_assignment[students[idx][1]] = score[idx // (N // 10)]

    # K 번째 학생의 학점 출력
    print(f"#{t} {grade_assignment[K]}")