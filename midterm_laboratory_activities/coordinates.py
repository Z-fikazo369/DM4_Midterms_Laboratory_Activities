# Part 2: Tuples & Sets Laboratory
#Note: This code already have a default user input instead of asking for user input directly for easy understanding of the behavior of the program.
import math

# Task 2.1: Coordinate System with Tuples
print("=" * 50)
print("TASK 2.1: COORDINATE SYSTEM WITH TUPLES")
print("=" * 50)

# Define three points as tuples
point1 = (2, 3)
point2 = (5, 7)
point3 = (1, 1)

def calculate_distance(p1, p2):
    """Calculate distance between two points using distance formula"""
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def find_midpoint(p1, p2):
    """Find the midpoint between two points"""
    x1, y1 = p1
    x2, y2 = p2
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    return midpoint

# Create a tuple containing all points
all_points = (point1, point2, point3)

print(f"\nDefined Points:")
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Point 3: {point3}")
print(f"\nAll points tuple: {all_points}")

# Test functions with sample coordinates
print(f"\n--- Testing Functions ---")
print(f"Distance between Point 1 and Point 2: {calculate_distance(point1, point2):.2f}")
print(f"Distance between Point 2 and Point 3: {calculate_distance(point2, point3):.2f}")
print(f"Distance between Point 1 and Point 3: {calculate_distance(point1, point3):.2f}")

print(f"\nMidpoint between Point 1 and Point 2: {find_midpoint(point1, point2)}")
print(f"Midpoint between Point 2 and Point 3: {find_midpoint(point2, point3)}")
print(f"Midpoint between Point 1 and Point 3: {find_midpoint(point1, point3)}")

# Demonstrate tuple immutability
print(f"\n--- Demonstrating Tuple Immutability ---")
print("Attempting to modify point1[0]...")
try:
    point1[0] = 10
except TypeError as e:
    print(f"Error: {e}")
    print("Tuples are immutable and cannot be modified!")

# Task 2.2: Unique Word Counter with Sets
print("\n" + "=" * 50)
print("TASK 2.2: UNIQUE WORD COUNTER WITH SETS")
print("=" * 50)

# Sample text
text = "Python is a programming language. Python is easy to learn. Python is powerful."

print(f"\nOriginal Text:")
print(f'"{text}"')

# Split text into words and clean them
words = text.lower().replace('.', '').split()

# Create set of unique words
unique_words = set(words)

# Count total words and unique words
total_words = len(words)
unique_word_count = len(unique_words)

print(f"\n--- Analysis ---")
print(f"Total words: {total_words}")
print(f"Unique words: {unique_word_count}")

print(f"\nUnique words set: {sorted(unique_words)}")

# Find the most common words
print(f"\n--- Word Frequency ---")
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Sort by frequency (descending)
sorted_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

print("Word frequencies:")
for word, count in sorted_frequency:
    print(f"  '{word}': {count} time(s)")

print(f"\nMost common word: '{sorted_frequency[0][0]}' appears {sorted_frequency[0][1]} times")