# 과제: 4개의 과목을 합계(개인평균, 전체 평균), 평균 (개인평균, 전체 평균)
# 홍길동1 {"국어": 95, '영어': 90, '수학': 80, '과학' : 50}
# 홍길동2 {"국어": 100, '영어': 50, '수학': 90, '과학' : 90}
# 홍길동3 {"국어": 99, '영어': 60, '수학': 100, '과학' : 40}
# 홍길동4 {"국어": 55, '영어': 80, '수학': 80, '과학' : 60}
# for / while / if/ elif 
# 7가지 방법으로 코드를 작성 : 결과는 모두 같아야 함

# 1 (잘못 이해함;)
# student1 = {"국어": 95, '영어': 90, '수학': 80, '과학' : 50}
# student2 = {"국어": 100, '영어': 50, '수학': 90, '과학' : 90}
# student3 = {"국어": 99, '영어': 60, '수학': 100, '과학' : 40}
# student4 = {"국어": 55, '영어': 80, '수학': 80, '과학' : 60}
# N = len(student1) # 과목 수
# score = [0]*N
# mean = [0]*N
# # 전체 합계, 전체 평균
# for i in range (N):
#     score[i] = score[i]+list(student1.values())[i]+list(student2.values())[i]+list(student3.values())[i]+list(student4.values())[i]
#     mean[i] = score[i]/N


# 1 
# 개인 평균 구하고 리스트에 입력
student1 = {"국어": 95, '영어': 90, '수학': 80, '과학' : 50}
student2 = {"국어": 100, '영어': 50, '수학': 90, '과학' : 90}
student3 = {"국어": 99, '영어': 60, '수학': 100, '과학' : 40}
student4 = {"국어": 55, '영어': 80, '수학': 80, '과학' : 60}

students = [student1, student2, student3, student4]
scores = []
means = []

for idx,i in enumerate (students):
    sum_ = sum(i.values())
    scores.append(sum_)
    mean_ = sum_/len(i)
    means.append(mean_)
    print ('학생',idx+1 ,'의 총점', sum_, '평균 ', mean_)

print ('전체 총점', sum(scores), '평균', sum(means)/len(students))



tmp = 1
