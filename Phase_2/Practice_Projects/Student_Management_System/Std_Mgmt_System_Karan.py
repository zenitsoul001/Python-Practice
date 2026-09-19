class StudentManagementSystem:

    def __init__(self):
        self.students = []
        self.run()

    # ==============================
    #       DISPLAY HEADER
    # ==============================

    def show_header(self):
        print("\n" + "=" * 60)
        print("           STUDENT MANAGEMENT SYSTEM")
        print("=" * 60)

    # ==============================
    #        ADD STUDENT
    # ==============================

    def add_student(self):

        print("\n" + "-" * 60)
        print("                    ADD STUDENT")
        print("-" * 60)

        name = input("Enter Student Name : ").strip()
        roll = input("Enter Roll Number  : ").strip()

        # Check duplicate roll number
        for student in self.students:
            if student["roll"] == roll:
                print("\n[ERROR] Roll number already exists!")
                return

        # Age validation
        while True:
            age = input("Enter Student Age  : ").strip()

            if age.isdigit():
                age = int(age)

                if age > 0:
                    break
                else:
                    print("[ERROR] Age must be greater than 0.")
            else:
                print("[ERROR] Please enter a valid age.")

        student = {
            "name": name,
            "roll": roll,
            "age": age
        }

        self.students.append(student)

        print("\n" + "-" * 60)
        print("        ✓ STUDENT ADDED SUCCESSFULLY")
        print("-" * 60)
        print(f"  Name       : {name}")
        print(f"  Roll Number: {roll}")
        print(f"  Age        : {age}")
        print("-" * 60)

    # ==============================
    #       VIEW STUDENTS
    # ==============================

    def view_students(self):

        print("\n" + "-" * 60)
        print("                    ALL STUDENTS")
        print("-" * 60)

        if not self.students:
            print("\n        No students found in the system.")
            print("        Please add a student first.")
            print("-" * 60)
            return

        print(f"{'No.':<5}{'Name':<25}{'Roll No.':<15}{'Age':<5}")
        print("-" * 60)

        for index, student in enumerate(self.students, start=1):
            print(
                f"{index:<5}"
                f"{student['name']:<25}"
                f"{student['roll']:<15}"
                f"{student['age']:<5}"
            )

        print("-" * 60)
        print(f"Total Students: {len(self.students)}")
        print("-" * 60)

    # ==============================
    #       FIND STUDENT
    # ==============================

    def find_student(self):

        print("\n" + "-" * 60)
        print("                    SEARCH STUDENT")
        print("-" * 60)

        roll_no = input("Enter Roll Number to search: ").strip()

        for student in self.students:

            if student["roll"] == roll_no:

                print("\n" + "-" * 60)
                print("              ✓ STUDENT FOUND")
                print("-" * 60)

                print(f"  Name        : {student['name']}")
                print(f"  Roll Number : {student['roll']}")
                print(f"  Age         : {student['age']}")

                print("-" * 60)
                return

        print("\n" + "-" * 60)
        print("              ✗ STUDENT NOT FOUND")
        print("-" * 60)
        print(f"  No student exists with Roll Number: {roll_no}")
        print("-" * 60)

    # ==============================
    #           MAIN MENU
    # ==============================

    def run(self):

        while True:

            self.show_header()

            print("\n  1.  View All Students")
            print("  2.  Add New Student")
            print("  3.  Search Student")
            print("  4.  Exit")

            print("\n" + "-" * 60)

            choice = input("  Enter your choice (1-4): ").strip()

            if choice == "1":
                self.view_students()

            elif choice == "2":
                self.add_student()

            elif choice == "3":
                self.find_student()

            elif choice == "4":
                print("\n" + "=" * 60)
                print("        Thank you for using Student Management System!")
                print("                    Goodbye! 👋")
                print("=" * 60)
                break

            else:
                print("\n" + "-" * 60)
                print("  [ERROR] Invalid choice!")
                print("  Please enter a number between 1 and 4.")
                print("-" * 60)


# ==============================
#       START APPLICATION
# ==============================

system = StudentManagementSystem()
