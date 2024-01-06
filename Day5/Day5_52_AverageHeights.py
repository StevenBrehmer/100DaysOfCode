
student_heights = [180,124,165,173,189,169,146]

print(str(type(student_heights)) + str(student_heights))
totalHeight = 0

for i in range(0,len(student_heights)):
    print(str(student_heights[i]))
    totalHeight += student_heights[i]

avgerageHeight = str(round(totalHeight/(i+1),2))
print(f"Avg Height: {avgerageHeight}")