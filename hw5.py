import os
import time

class Student:
    def __init__(self):
        self.students = {}   # store all students here

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def add_student(self):
        self.clear()
        print("=== Add Student ===")
        sid = input("Enter ID: ")
        if sid in self.students:
            print("❌ Student ID already exists!")
        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            self.students[sid] = {"name": name, "age": age, "grade": grade}
            print("✔️ Student added!")
        time.sleep(1.5)

    def remove_student(self):
        self.clear()
        sid = input("Enter Student ID to remove: ")
        if sid in self.students:
            del self.students[sid]
            print("✔️ Student removed!")
        else:
            print("❌ Student not found.")
        time.sleep(1.5)

    def update_student(self):
        self.clear()
        sid = input("Enter Student ID to update: ")

        if sid in self.students:
            print("Leave blank to skip.")
            name = input("New Name: ")
            age = input("New Age: ")
            grade = input("New Grade: ")

            if name: self.students[sid]["name"] = name
            if age: self.students[sid]["age"] = age
            if grade: self.students[sid]["grade"] = grade

            print("✔️ Student updated!")
        else:
            print("❌ Student not found.")
        time.sleep(1.5)

    def search_student(self):
        self.clear()
        sid = input("Enter Student ID: ")
        student = self.students.get(sid)

        if student:
            print("\n✔️ Student Found:")
            print(f"ID: {sid}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
        else:
            print("❌ Student NOT found.")
        input("\nPress ENTER to continue...")

    def display_students(self):
        self.clear()
        if not self.students:
            print("No students available.")
        else:
            print("=== All Students ===\n")
            for sid, info in self.students.items():
                print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")
        input("\nPress ENTER to continue...")

    def menu(self):
        while True:
            self.clear()
            print("===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Update Student")
            print("4. Search Student")
            print("5. Display All Students")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.search_student()
            elif choice == "5":
                self.display_students()
            elif choice == "6":
                self.clear()
                print("Goodbye!")
                break
            else:
                print("❌ Invalid choice!")
                time.sleep(1.5)


# Run the program
system = Student()
system.menu()

