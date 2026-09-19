class Student:

    def __init__(self, rollno, name, course, marks):

        self.rollno = rollno
        self.name = name
        self.course = course
        self.marks = marks


    def show_details(self):

        print("╔" + "═" * 39 + "╗")
        print(f"║  🎓 Roll Number : {self.rollno:<20}║")
        print(f"║  👤 Name        : {self.name:<20}║")
        print(f"║  📚 Course      : {self.course:<20}║")
        print(f"║  📊 Marks       : {self.marks:<20}║")
        print("╚" + "═" * 39 + "╝")


class StudentManagementSystem:

    def __init__(self):

        # Saare Student objects is list mein store honge
        self.students = []


    def add_students(self, rollno, name, course, marks):

        # Naya Student object create kiya
        student = Student(
            rollno,
            name,
            course,
            marks
        )

        # Student ko list mein add kiya
        self.students.append(student)

        print("\n✅ Student Added Successfully!\n")


    def view_students(self):

        if not self.students:

            print("\nNo Students Added Yet!\n")
            return


        print("\n")
        print("╔" + "═" * 45 + "╗")
        print("║            📚 ALL STUDENTS 📚               ║")
        print("╚" + "═" * 45 + "╝")


        for student in self.students:

            student.show_details()
            print()


    def search_student(self, rollno):

        for student in self.students:

            if student.rollno == rollno:

                print("\n🔍 Student Found!\n")

                student.show_details()

                return


        print("\n❌ Student Not Found!\n")


    def run(self):

        while True:

            print("\n")
            print("╔" + "═" * 46 + "╗")
            print("║        🎓 STUDENT MANAGEMENT SYSTEM 🎓       ║")
            print("╠" + "═" * 46 + "╣")
            print("║                                              ║")
            print("║   1️⃣   View All Students                      ║")
            print("║   2️⃣   Add New Student                        ║")
            print("║   3️⃣   Search Student                         ║")
            print("║   4️⃣   Exit                                   ║")
            print("║                                              ║")
            print("╚" + "═" * 46 + "╝")


            try:

                choice = int(
                    input("\n👉 Choose your action (1-4): ")
                )

            except ValueError:

                print("\n❌ Invalid Input!")
                print("Please enter only 1, 2, 3 or 4.")

                continue


            # =========================
            # VIEW STUDENTS
            # =========================

            if choice == 1:

                self.view_students()


            # =========================
            # ADD STUDENT
            # =========================

            elif choice == 2:

                print("\n")
                print("┌" + "─" * 40 + "┐")
                print("│         ➕ ADD NEW STUDENT             │")
                print("└" + "─" * 40 + "┘")


                try:

                    rollno = int(
                        input("🎓 Enter Roll Number : ")
                    )

                    name = input(
                        "👤 Enter Student Name : "
                    )

                    course = input(
                        "📚 Enter Course       : "
                    )

                    marks = float(
                        input("📊 Enter Marks        : ")
                    )


                    self.add_students(
                        rollno,
                        name,
                        course,
                        marks
                    )


                except ValueError:

                    print("\n❌ Invalid Data!")
                    print(
                        "Roll Number and Marks must be numeric."
                    )


            # =========================
            # SEARCH STUDENT
            # =========================

            elif choice == 3:

                print("\n")
                print("┌" + "─" * 40 + "┐")
                print("│          🔍 SEARCH STUDENT             │")
                print("└" + "─" * 40 + "┘")


                try:

                    rollno = int(
                        input("🎓 Enter Roll Number to Search : ")
                    )

                    self.search_student(
                        rollno
                    )


                except ValueError:

                    print(
                        "\n❌ Please enter a valid Roll Number."
                    )


            # =========================
            # EXIT
            # =========================

            elif choice == 4:

                print("\n")
                print("╔" + "═" * 48 + "╗")
                print("║                                                ║")
                print("║        👋 Thank You For Using SMS!             ║")
                print("║               Goodbye!                         ║")
                print("║                                                ║")
                print("╚" + "═" * 48 + "╝")

                break


            else:

                print(
                    "\n⚠️ Please choose only 1, 2, 3 or 4."
                )


# ==========================================
# PROGRAM START
# ==========================================

system = StudentManagementSystem()

system.run()