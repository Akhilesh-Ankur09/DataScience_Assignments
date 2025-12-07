# -------------------------------
# TASK 1: BASIC OPERATIONS
# -------------------------------

# Accept two integer inputs from the user
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

# Perform arithmetic operations using basic operators
add_result = a + b            # Addition
sub_result = a - b            # Subtraction
mul_result = a * b            # Multiplication

# For division and modulus, we check if b is not zero to avoid error
if b != 0:
    div_result = a / b        # Division
    mod_result = a % b        # Modulus
else:
    div_result = "undefined (division by zero)"
    mod_result = "undefined (modulus by zero)"

exp_result = a ** b           # Exponentiation

# Print all results in a well-formatted way using f-strings
print("\n----- TASK 1: Arithmetic Operations -----")
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {add_result}")
print(f"Subtraction: {a} - {b} = {sub_result}")
print(f"Multiplication: {a} * {b} = {mul_result}")
print(f"Division: {a} / {b} = {div_result}")
print(f"Modulus: {a} % {b} = {mod_result}")
print(f"Exponentiation: {a} ** {b} = {exp_result}")


# -------------------------------
# TASK 2: WORKING WITH LISTS AND ARRAYS
# -------------------------------

# We need NumPy for array operations (mean, median, std)
import numpy as np

# 1. Create a list containing at least 10 numbers
num_list = [10, 25, 37, 49, 52, 63, 71, 84, 95, 100]

print("\n----- TASK 2: List and NumPy Array Operations -----")

# 2(a). Print the length of the list
print(f"Original list: {num_list}")
print(f"Length of the list: {len(num_list)}")

# 2(b). Find the maximum and minimum value
max_value = max(num_list)
min_value = min(num_list)
print(f"Maximum value in the list: {max_value}")
print(f"Minimum value in the list: {min_value}")

# 2(c). Add a new element and remove one element
# Adding a new element at the end
num_list.append(120)  # New element
# Removing an element (here we remove the first occurrence of 37 for example)
num_list.remove(37)

print(f"List after adding 120 and removing 37: {num_list}")

# 2(d). Sort the list in ascending and descending order
ascending_list = sorted(num_list)
descending_list = sorted(num_list, reverse=True)

print(f"List in ascending order: {ascending_list}")
print(f"List in descending order: {descending_list}")

# 3. Convert the list into a NumPy array
num_array = np.array(num_list)

# Calculate Mean, Median, and Standard Deviation
mean_value = np.mean(num_array)
median_value = np.median(num_array)
std_value = np.std(num_array)

print("\nNumPy Array Calculations:")
print(f"Array: {num_array}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_value}")


# -------------------------------
# TASK 3: DICTIONARIES AND SETS
# -------------------------------

print("\n----- TASK 3: Dictionaries and Sets -----")

# 1. Create a dictionary named student with keys: name, age, course, marks
student = {
    "name": "Akhilesh",
    "age": 25,
    "course": "Data Science",
    "marks": 88
}

# 2. Print each key-value pair using a loop
print("\nStudent Dictionary (key-value pairs):")
for key, value in student.items():
    print(f"{key}: {value}")

# 3. Add a new key called grade with a value of your choice
student["grade"] = "A"

print("\nStudent Dictionary after adding 'grade':")
for key, value in student.items():
    print(f"{key}: {value}")

# 4. Create a set of unique courses (duplicate "Python" included intentionally)
courses_set = {"Python", "Data Science", "AI", "Python"}
print("\nSet of unique courses:")
print(courses_set)  # Set automatically removes duplicate "Python"

# 5. Perform set operations — union, intersection, and difference — between two sets
set1 = {"Python", "Data Science", "ML"}
set2 = {"AI", "Python", "DL"}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)   # Elements in set1 but not in set2

print("\nSet Operations:")
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union (set1 ∪ set2): {union_set}")
print(f"Intersection (set1 ∩ set2): {intersection_set}")
print(f"Difference (set1 - set2): {difference_set}")


# -------------------------------
# TASK 4: FILE HANDLING
# -------------------------------

print("\n----- TASK 4: File Handling -----")

# 1. Create a text file named student_data.txt
# 2. Write name, course, and marks of at least 5 students into the file
with open("student_data.txt", "w") as f:
    # Each line: name, course, marks
    f.write("Rahul, Data Science, 82\n")
    f.write("Sneha, Python, 74\n")
    f.write("Aman, AI, 90\n")
    f.write("Neha, ML, 78\n")
    f.write("Karan, Data Science, 68\n")

print("student_data.txt file created and data written successfully.")

# 3. Read the file and display only those students whose marks are above 75
print("\nStudents with marks above 75:")

with open("student_data.txt", "r") as f:
    for line in f:
        # Remove extra spaces/newlines and split by comma
        line = line.strip()
        if not line:
            continue
        name, course, marks_str = line.split(", ")
        marks = int(marks_str)

        # Check if marks are above 75
        if marks > 75:
            print(f"Name: {name}, Course: {course}, Marks: {marks}")