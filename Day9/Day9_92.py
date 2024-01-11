student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#print(student_scores)
student_grades= {}

for name in student_scores:
    grade =""
    if student_scores[name] >=91:
        grade = "Outstanding"
    elif student_scores[name] >=81:
        grade = "Exceeds Expectations"
    elif student_scores[name] >=71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[name] = grade

print(student_grades)