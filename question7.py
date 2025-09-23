def calculate_marks(marks_list):
    highest = max(marks_list)
    lowest = min(marks_list)
    average = sum(marks_list) / len(marks_list)
    
    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"
    
    return highest, lowest, average, grade

marks = list(map(int, input("Enter marks of 5 students : ").split()))

h, l, avg, g = calculate_marks(marks)
print(f"Highest: {h}, Lowest: {l}, Average: {avg:.2f}, Grade: {g}")