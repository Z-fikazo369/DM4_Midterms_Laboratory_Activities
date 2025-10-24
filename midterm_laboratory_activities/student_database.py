# Part 3: Dictionaries Laboratory
#Note: This code is user interactive compared to the previous files for indepth understanding of dictionary operations.


# Task 3.1: Student Database
print("=" * 50)
print("TASK 3.1: STUDENT DATABASE")
print("=" * 50)

# Create empty dictionary for students
students = {}

def add_student(student_id, name, grade, major):
    """Add a student with ID, name, grade, and major"""
    students[student_id] = {
        'name': name,
        'grade': grade,
        'major': major
    }
    print(f"Added student: {name} (ID: {student_id})")

def retrieve_student(student_id):
    """Retrieve student information by ID"""
    if student_id in students:
        return students[student_id]
    else:
        return None

def update_grade(student_id, new_grade):
    """Update a student's grade"""
    if student_id in students:
        old_grade = students[student_id]['grade']
        students[student_id]['grade'] = new_grade
        print(f"Updated {students[student_id]['name']}'s grade from {old_grade} to {new_grade}")
    else:
        print(f"Student with ID {student_id} not found")

def display_all_students():
    """Display all students"""
    print("\n--- All Students ---")
    if not students:
        print("No students in database")
    else:
        for student_id, info in students.items():
            print(f"ID: {student_id}")
            print(f"  Name: {info['name']}")
            print(f"  Grade: {info['grade']}")
            print(f"  Major: {info['major']}")
            print()

# Interactive menu
while True:
    print("\n=== STUDENT DATABASE MENU ===")
    print("1. Add Student")
    print("2. Retrieve Student")
    print("3. Update Grade")
    print("4. Display All Students")
    print("5. Exit to Task 3.2")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        grade = input("Enter Grade: ")
        major = input("Enter Major: ")
        add_student(student_id, name, grade, major)
    
    elif choice == "2":
        print("\n--- Retrieve Student ---")
        student_id = input("Enter Student ID: ")
        student_info = retrieve_student(student_id)
        if student_info:
            print(f"\nStudent Found:")
            print(f"  Name: {student_info['name']}")
            print(f"  Grade: {student_info['grade']}")
            print(f"  Major: {student_info['major']}")
        else:
            print("Student not found")
    
    elif choice == "3":
        print("\n--- Update Grade ---")
        student_id = input("Enter Student ID: ")
        new_grade = input("Enter New Grade: ")
        update_grade(student_id, new_grade)
    
    elif choice == "4":
        display_all_students()
    
    elif choice == "5":
        print("\nExiting to Task 3.2...")
        break
    
    else:
        print("Invalid choice! Please enter 1-5")

# Task 3.2: Word Frequency Counter
print("\n" + "=" * 50)
print("TASK 3.2: WORD FREQUENCY COUNTER")
print("=" * 50)

# Get text input from user
print("\nEnter your text (2-3 sentences):")
print("(Press Enter after typing your text)")
text = input()

# Convert to lowercase and split into words (remove punctuation)
words = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()

# Count word frequencies using dictionary
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(f"\n--- Word Frequency Analysis ---")
print(f"Total words: {len(words)}")
print(f"Unique words: {len(word_frequency)}")

# Display words sorted by frequency (descending)
print("\n--- Words Sorted by Frequency ---")
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"  '{word}': {count} time(s)")

# Identify the most common word
if sorted_words:
    most_common_word = sorted_words[0][0]
    most_common_count = sorted_words[0][1]
    
    print(f"\n--- Most Common Word ---")
    print(f"The word '{most_common_word}' appears {most_common_count} times")