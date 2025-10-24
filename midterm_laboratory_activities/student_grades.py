# Part 1: Lists Laboratory
# Task 1.1: Student Grade Manager
#Note: This code already have a default user input instead of asking for user input directly for easy understanding of the behavior of the program.
print("=" * 50)
print("TASK 1.1: STUDENT GRADE MANAGER")
print("=" * 50)

# Create empty lists
student_names = []
student_grades = []
# Mga fuctions to manage student grades
def add_student(name, grade):
    """Add a student and their grade to the lists"""
    student_names.append(name)
    student_grades.append(grade)
    print(f"Added {name} with grade {grade}")

def calculate_average():
    """Calculate the average grade"""
    if len(student_grades) == 0:
        return 0
    return sum(student_grades) / len(student_grades)

def find_highest_grade():
    """Find the highest grade"""
    if len(student_grades) == 0:
        return None
    return max(student_grades)

def display_students():
    """Display all students and their grades"""
    print("\nStudent Grades:")
    for i in range(len(student_names)):
        print(f"{student_names[i]}: {student_grades[i]}")

# 3 sample students
add_student("Alice", 85)
add_student("Bob", 92)
add_student("Charlie", 78)

# Display results
display_students()

print(f"\nAverage Grade: {calculate_average()}")
print(f"Highest Grade: {find_highest_grade()}")

# Task 1.2: List Operations Practice
print("\n" + "=" * 50)
print("TASK 1.2: LIST OPERATIONS PRACTICE")
print("=" * 50)

# Create list of numbers
numbers = [5, 2, 8, 1, 9, 3]
print(f"\nOriginal list: {numbers}")

# Sort the list
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

# Calculate the sum
total_sum = sum(numbers)
print(f"Sum: {total_sum}")

# Calculate the average
average = sum(numbers) / len(numbers)
print(f"Average: {average:.2f}")

# Find maximum and minimum values
maximum = max(numbers)
minimum = min(numbers)
print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")

# Find the list length
length = len(numbers)
print(f"List length: {length}")