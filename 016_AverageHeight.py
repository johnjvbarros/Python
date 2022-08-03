# 🚨 Don't change the code below 👇
student_heights = input(
    "Input a list of student heights (separate by space)").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
height_sum = sum(student_heights)
height_qt = len(student_heights)

avg_height = round(height_sum / height_qt)

print(avg_height)
