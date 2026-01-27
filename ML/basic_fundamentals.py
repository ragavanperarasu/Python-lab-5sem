student_ids = ("S101", "S102", "S103", "S104")

students = {
    "S101": {"name": "Alice", "assignment": 78, "test": 65, "attendence": 89, "hours": 6},
    "S102": {"name": "Bob", "assignment": 79, "test": 76, "attendence": 90, "hours": 5},
    "S103": {"name": "Charlie", "assignment": 89, "test": 78, "attendence": 80, "hours": 5},
    "S104": {"name": "David", "assignment": 90, "test": 90, "attendence": 97, "hours": 6}
}

def calculate_average(assignment, test):
    return (assignment + test) / 2

def determine_risk(avg_score, attendence, hours):
    if avg_score >= 75 and attendence >= 85 and hours >= 5:
        return "Low Risk"
    elif avg_score >= 60 and attendence >= 85:
        return "Medium Risk"
    else:
        return "High Risk"

print("\nSTUDENT PERFORMANCE REPORT")
print("-" * 40)

for sid in student_ids:
    student = students.get(sid)

    if student is None:
        print(f"Student ID {sid} not found. Skipping.")
        continue

    avg_score = calculate_average(
        student["assignment"],
        student["test"]
    )

    risk = determine_risk(
        avg_score,
        student["attendence"],
        student["hours"]
    )

    print(f"""
Student ID     : {sid}
Name           : {student["name"]}
Assignment     : {student["assignment"]}
Test Score     : {student["test"]}
Attendence     : {student["attendence"]}
Study Hours    : {student["hours"]}
Average Score  : {avg_score:.2f}
Risk Level     : {risk}
----------------------------------------------
""")