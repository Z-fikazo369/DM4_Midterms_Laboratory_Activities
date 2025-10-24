# Part 4: File Handling Laboratory
#Note: This code is user interactive compared to the previous files for indepth understanding of dictionary operations.

import pickle
import os

# Task 4.1: Student Records File System
print("=" * 50)
print("TASK 4.1: STUDENT RECORDS FILE SYSTEM")
print("=" * 50)

def save_students_pickle(students, filename):
    """Save student records using pickle"""
    try:
        with open(filename, 'wb') as file:
            pickle.dump(students, file)
        print(f"✓ Successfully saved {len(students)} student(s) to {filename}")
        return True
    except Exception as e:
        print(f"✗ Error saving file: {e}")
        return False

def load_students_pickle(filename):
    """Load student records from pickle files"""
    try:
        with open(filename, 'rb') as file:
            students = pickle.load(file)
        print(f"✓ Successfully loaded {len(students)} student(s) from {filename}")
        return students
    except FileNotFoundError:
        print(f"✗ File {filename} not found")
        return {}
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return {}

def export_students_text(students, filename):
    """Export student records to a readable text file"""
    try:
        with open(filename, 'w') as file:
            file.write("=" * 50 + "\n")
            file.write("STUDENT RECORDS\n")
            file.write("=" * 50 + "\n\n")
            
            if not students:
                file.write("No students in database\n")
            else:
                for student_id, info in students.items():
                    file.write(f"Student ID: {student_id}\n")
                    file.write(f"  Name: {info['name']}\n")
                    file.write(f"  Grade: {info['grade']}\n")
                    file.write(f"  Major: {info['major']}\n")
                    file.write("-" * 50 + "\n")
        
        print(f"✓ Successfully exported students to {filename}")
        return True
    except Exception as e:
        print(f"✗ Error exporting file: {e}")
        return False

def display_students(students):
    """Display all students"""
    if not students:
        print("No students in database")
    else:
        print("\n--- Current Students ---")
        for student_id, info in students.items():
            print(f"ID: {student_id}")
            print(f"  Name: {info['name']}")
            print(f"  Grade: {info['grade']}")
            print(f"  Major: {info['major']}")
            print()

# Initialize student dictionary
students = {}

# Interactive menu for Task 4.1
while True:
    print("\n=== STUDENT RECORDS FILE SYSTEM MENU ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Save Students to Pickle File")
    print("4. Load Students from Pickle File")
    print("5. Export Students to Text File")
    print("6. Exit to Task 4.2")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == "1":
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        grade = input("Enter Grade: ")
        major = input("Enter Major: ")
        
        students[student_id] = {
            "name": name,
            "grade": grade,
            "major": major
        }
        print(f"✓ Added student: {name}")
    
    elif choice == "2":
        display_students(students)
    
    elif choice == "3":
        filename = input("Enter filename to save (e.g., students.pkl): ")
        save_students_pickle(students, filename)
    
    elif choice == "4":
        filename = input("Enter filename to load (e.g., students.pkl): ")
        loaded = load_students_pickle(filename)
        if loaded:
            students = loaded
            display_students(students)
    
    elif choice == "5":
        filename = input("Enter filename to export (e.g., students.txt): ")
        export_students_text(students, filename)
    
    elif choice == "6":
        print("\nExiting to Task 4.2...")
        break
    
    else:
        print("Invalid choice! Please enter 1-6")

# Task 4.2: File Operations Practice
print("\n" + "=" * 50)
print("TASK 4.2: FILE OPERATIONS PRACTICE")
print("=" * 50)

# Interactive menu for Task 4.2
while True:
    print("\n=== FILE OPERATIONS MENU ===")
    print("1. Write to a New File ('w' mode)")
    print("2. Read from a File ('r' mode)")
    print("3. Append to a File ('a' mode)")
    print("4. Demonstrate File Not Found Error")
    print("5. Exit Program")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
        print("\n--- Writing to a New File ('w' mode) ---")
        filename = input("Enter filename to create: ")
        print("Enter content (type 'DONE' on a new line when finished):")
        lines = []
        while True:
            line = input()
            if line == "DONE":
                break
            lines.append(line + "\n")
        
        try:
            with open(filename, 'w') as file:
                file.writelines(lines)
            print(f"✓ Successfully wrote to {filename}")
        except Exception as e:
            print(f"✗ Error writing file: {e}")
    
    elif choice == "2":
        print("\n--- Reading from a File ('r' mode) ---")
        filename = input("Enter filename to read: ")
        try:
            with open(filename, 'r') as file:
                content = file.read()
            print(f"✓ Successfully read from {filename}")
            print("\n--- File Contents ---")
            print(content)
        except FileNotFoundError:
            print(f"✗ File '{filename}' not found!")
        except Exception as e:
            print(f"✗ Error reading file: {e}")
    
    elif choice == "3":
        print("\n--- Appending to a File ('a' mode) ---")
        filename = input("Enter filename to append to: ")
        print("Enter content to append (type 'DONE' on a new line when finished):")
        lines = []
        while True:
            line = input()
            if line == "DONE":
                break
            lines.append(line + "\n")
        
        try:
            with open(filename, 'a') as file:
                file.writelines(lines)
            print(f"✓ Successfully appended to {filename}")
            
            # Show updated content
            print("\n--- Updated File Contents ---")
            with open(filename, 'r') as file:
                content = file.read()
            print(content)
        except Exception as e:
            print(f"✗ Error appending to file: {e}")
    
    elif choice == "4":
        print("\n--- Demonstrating File Not Found Error Handling ---")
        filename = input("Enter a non-existent filename: ")
        try:
            with open(filename, 'r') as file:
                content = file.read()
            print(f"✓ File found and read successfully")
        except FileNotFoundError:
            print(f"✗ Error: The file '{filename}' does not exist!")
            print("  This error was caught and handled gracefully.")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
    
    elif choice == "5":
        print("\n" + "=" * 50)
        print("FILE HANDLING LABORATORY COMPLETED")
        print("=" * 50)
        print("\nThank you for using the File Handling Laboratory!")
        break
    
    else:
        print("Invalid choice! Please enter 1-5")