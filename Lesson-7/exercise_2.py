from bisect import bisect

input_grade = int(input("Enter your grade: "))
grades = [0, 21, 41, 66, 86, 101]
grade = [1, 2, 3, 4, 5, "100 dan katta ball berib bo'lmaydi."]
i = bisect(grades, input_grade, 0, 6)
print(grade[i-1])
