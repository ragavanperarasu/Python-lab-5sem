from datetime import datetime

# Student records (example data)
students = {
    "ragavan": {"marks": 90, "assignment": True},
    "arun": {"marks": 85, "assignment": False},
    "karthik": {"marks": 78, "assignment": True},
    "siva": {"marks": 88, "assignment": False},
    "mani": {"marks": 92, "assignment": True}
}

# Function to write logs
def write_log(name, activity):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open("student_activity_log.txt", "a") as file:
        file.write(f"{name}, {activity}, {date}, {time}\n")

# Menu
print("1. View Marks")
print("2. Update Assignment Status")

choice = input("Enter your choice (1 or 2): ")
name = input("Enter student name: ").lower()

if name not in students:
    print("Student not found!")
else:
    if choice == "1":
        marks = students[name]["marks"]
        print(f"{name}'s marks: {marks}")
        write_log(name, "Viewed Marks")

    elif choice == "2":
        status = input("Assignment submitted? (yes/no): ").lower()
        students[name]["assignment"] = True if status == "yes" else False
        print("Assignment status updated.")
        write_log(name, "Updated Assignment Status")

    else:
        print("Invalid choice!")
