students = [
    {"name": "Alice", "ID": 101, "marks": 85},
    {"name": "Bob", "ID": 102, "marks": 78},
    {"name": "Charlie", "ID": 103, "marks": 92},
    {"name": "David", "ID": 104, "marks": 60},
    {"name": "Eva", "ID": 105, "marks": 70}
]

def add_student():
    name = input("Enter student name: ")
    ID = int(input("Enter student ID: "))
    marks = int(input("Enter marks: "))
    students.append({"name": name, "ID": ID, "marks": marks})
    print("Student added!")

def search_student():
    ID = int(input("Enter student ID to search: "))
    for student in students:
        if student["ID"] == ID:
            print(student)
            return
    print("Student not found.")

def display_students():
    sorted_list = sorted(students, key=lambda x: x["marks"], reverse=True)
    for student in sorted_list:
        print(student)

# Menu
while True:
    print("\n1. Add Student\n2. Search Student\n3. Display All\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        display_students()
    elif choice == '4':
        break
    else:
        print("Invalid choice")