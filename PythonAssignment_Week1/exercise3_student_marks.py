# -------------------------------------------------
# Exercise 3: Student Marks Processor
# -------------------------------------------------
# This program:
# 1. Reads student data from an external CSV file
# 2. Calculates overall marks using weightage
# 3. Assigns grades based on overall marks
# 4. Stores data in a NumPy structured array
# 5. Sorts students by overall marks
# 6. Writes results to an output file
# 7. Displays grade statistics
# -------------------------------------------------

import numpy as np

try:
    input_file = "student_marks.txt"
    output_file = "student_results.txt"

    students = []

    # Open and read external student marks file
    with open(input_file, "r") as f:
        header = f.readline()  # skip header line

        for line in f:
            roll_no, name, exam, coursework = line.strip().split(",")

            exam = float(exam)
            coursework = float(coursework)

            # Calculate overall mark
            # Exam = 60%, Coursework = 40%
            overall = (0.6 * exam) + (0.4 * coursework)

            # Grade assignment
            if overall >= 80:
                grade = "A"
            elif overall >= 70:
                grade = "B"
            elif overall >= 60:
                grade = "C"
            else:
                grade = "F"

            students.append(
                (roll_no, name, exam, coursework, overall, grade)
            )

    # Define NumPy structured array
    dtype = [
        ("roll_no", "U10"),
        ("name", "U30"),
        ("exam", "f4"),
        ("coursework", "f4"),
        ("overall", "f4"),
        ("grade", "U1")
    ]

    data = np.array(students, dtype=dtype)

    # Sort students by overall marks (descending)
    data = np.sort(data, order="overall")[::-1]

    # Write results to output file
    with open(output_file, "w") as f:
        f.write("roll_number,name,overall_mark,grade\n")
        for s in data:
            f.write(
                f"{s['roll_no']},{s['name']},{s['overall']:.2f},{s['grade']}\n"
            )

    # Display grade statistics
    print("Grade Statistics:")
    unique, counts = np.unique(data["grade"], return_counts=True)
    for g, c in zip(unique, counts):
        print(f"Grade {g}: {c} students")

except FileNotFoundError:
    print("Error: student_marks.txt file not found.")

except Exception as e:
    print("Error processing student data:", e)
