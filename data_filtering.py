
# Simple Data Filtering
# Veda Technology Internship - Task 8

STUDENTS = [
    {
        "student_id": "S101",
        "name": "Arun",
        "age": 20,
        "department": "Computer Science",
        "marks": 85
    },
    {
        "student_id": "S102",
        "name": "Priya",
        "age": 21,
        "department": "Data Science",
        "marks": 92
    },
    {
        "student_id": "S103",
        "name": "Rahul",
        "age": 19,
        "department": "Artificial Intelligence",
        "marks": 76
    },
    {
        "student_id": "S104",
        "name": "Sneha",
        "age": 22,
        "department": "Computer Science",
        "marks": 68
    },
    {
        "student_id": "S105",
        "name": "Kiran",
        "age": 20,
        "department": "Data Science",
        "marks": 81
    },
    {
        "student_id": "S106",
        "name": "Ananya",
        "age": 18,
        "department": "Electronics",
        "marks": 95
    },
    {
        "student_id": "S107",
        "name": "Vikram",
        "age": 23,
        "department": "Computer Science",
        "marks": 74
    },
    {
        "student_id": "S108",
        "name": "Meera",
        "age": 21,
        "department": "Artificial Intelligence",
        "marks": 88
    }
]


def display_students(students):
    """Display filtered student records in a readable table."""

    if not students:
        print("\nNo students match the selected condition.")
        return

    print("\n" + "=" * 92)
    print(
        f"{'ID':<10}{'Name':<14}{'Age':<8}"
        f"{'Department':<32}{'Marks':>8}"
    )
    print("-" * 92)

    for student in students:
        print(
            f"{student['student_id']:<10}"
            f"{student['name']:<14}"
            f"{student['age']:<8}"
            f"{student['department']:<32}"
            f"{student['marks']:>8}"
        )

    print("-" * 92)
    print(f"Total matching students: {len(students)}")


def filter_by_marks(students, minimum_marks):
    """Return students whose marks meet the minimum."""
    return [
        student for student in students
        if student["marks"] >= minimum_marks
    ]


def filter_by_age(students, maximum_age):
    """Return students whose age is below the maximum."""
    return [
        student for student in students
        if student["age"] < maximum_age
    ]


def filter_by_department(students, department):
    """Return students from a selected department."""
    return [
        student for student in students
        if student["department"].casefold()
        == department.strip().casefold()
    ]


def filter_by_multiple_conditions(
    students, minimum_marks, maximum_age
):
    """Return students meeting both conditions."""
    return [
        student for student in students
        if student["marks"] >= minimum_marks
        and student["age"] < maximum_age
    ]


def show_all_students(students):
    """Display the complete student dataset."""
    print("\nALL STUDENT RECORDS")
    display_students(students)


def main():
    while True:
        print("\n" + "=" * 45)
        print("       SIMPLE DATA FILTERING SYSTEM")
        print("=" * 45)
        print("1. Display all students")
        print("2. Filter by minimum marks")
        print("3. Filter by maximum age")
        print("4. Filter by department")
        print("5. Filter by marks AND age")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_all_students(STUDENTS)

        elif choice == "2":
            try:
                minimum = float(
                    input("Enter minimum marks (0-100): ")
                )

                if not 0 <= minimum <= 100:
                    print("Marks must be between 0 and 100.")
                    continue

                result = filter_by_marks(STUDENTS, minimum)
                print(f"\nStudents with marks >= {minimum:g}")
                display_students(result)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            try:
                maximum = int(input("Enter maximum age: "))

                if maximum <= 0:
                    print("Age must be a positive number.")
                    continue

                result = filter_by_age(STUDENTS, maximum)
                print(f"\nStudents younger than {maximum}")
                display_students(result)

            except ValueError:
                print("Please enter a valid whole number for age.")

        elif choice == "4":
            print("\nAvailable departments:")
            departments = sorted({
                student["department"] for student in STUDENTS
            })

            for department in departments:
                print(f"- {department}")

            department = input(
                "Enter department name: "
            ).strip()

            result = filter_by_department(STUDENTS, department)
            print(f"\nDepartment filter: {department}")
            display_students(result)

        elif choice == "5":
            try:
                minimum = float(
                    input("Enter minimum marks (0-100): ")
                )
                maximum = int(input("Enter maximum age: "))

                if not 0 <= minimum <= 100:
                    print("Marks must be between 0 and 100.")
                    continue

                if maximum <= 0:
                    print("Age must be a positive number.")
                    continue

                result = filter_by_multiple_conditions(
                    STUDENTS, minimum, maximum
                )

                print(
                    f"\nStudents with marks >= {minimum:g} "
                    f"AND age < {maximum}"
                )
                display_students(result)

            except ValueError:
                print("Enter valid numeric values.")

        elif choice == "6":
            print("Thank you for using the filtering system.")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
