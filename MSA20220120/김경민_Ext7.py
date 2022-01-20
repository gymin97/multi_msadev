student1 = ['국어', 95, '영어', 90, '수학', 80, '과학', 50]
student2 = ['국어', 100, '영어', 50, '수학', 90, '과학', 90]
student3 = ['국어', 99, '영어', 60, '수학', 100, '과학', 40]
student4 = ['국어', 55, '영어', 80, '수학', 80, '과학', 60]

students = [student1, student2, student3, student4]
scores = []
means = []

for idx, stu in enumerate (students):
    hap = 0
    for s in stu[1::2]:
        hap = hap + s
    scores.append(hap)
    means.append(hap / len(stu[1::2]))
    print ('학생',idx+1 ,'의 총점', scores[idx], '평균 ', means[idx])

    
print ('전체 총점', sum(scores), '평균', sum(means)/len(students))

tmp = 1 