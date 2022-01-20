# 5
student1 = {"국어": 95, '영어': 90, '수학': 80, '과학' : 50}
student2 = {"국어": 100, '영어': 50, '수학': 90, '과학' : 90}
student3 = {"국어": 99, '영어': 60, '수학': 100, '과학' : 40}
student4 = {"국어": 55, '영어': 80, '수학': 80, '과학' : 60}

students = [student1, student2, student3, student4]
scores = []
means = []

for stud in students:
    N = 0
    hap = 0
    while N < len(stud.values()):
        hap = hap + list(stud.values())[N]
        N = N + 1
    scores.append(hap)
    means.append(hap/len(student1))
    print ('총점', hap, '평균 ', hap/len(student1))


print ('전체 총점', sum(scores), '평균', sum(means)/len(students))

tmp = 1