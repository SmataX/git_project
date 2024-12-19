from src.student_handler import StudentHandler
from src.storage_handler import read_from_file

def display_menu():
    print("----- Students Manager -----")
    print("[1] list of students")
    print("[2] add student")
    print("[3] remove student")
    print("[4] edit student")
    print("[0] exit")


def main():
    student_handler = StudentHandler(list_of_students=read_from_file("data/students.csv"))

    while True:
        display_menu()

        user_input = -1
        while user_input not in [0, 1, 2, 3, 4]:
            try:
                user_input = int(input("Select option: "))
            except ValueError:
                pass
            print("-- incorrect value")

        # quit app
        if user_input == 0:
            break
        
        # list of students
        elif user_input == 1:
            print("\n----- LIST OF STUDENTS -----")
            for student in student_handler.list_of_students:
                print(f"[{student[0]}] {student[1]} {student[2]}")

        # add student
        elif user_input == 2:
            print("\n----- ADD STUDENT -----")
            first_name = input("Enter firstname: ")
            surname = input("Enter surname: ")
            student_handler.add_student(student_handler.generate_id(), first_name=first_name, surname=surname)

        # remove student
        elif user_input == 3:
            print("\n----- REMOVE STUDENT -----")
            for student in student_handler.list_of_students:
                print(f"[{student[0]}] {student[1]} {student[2]}")

        print("\n\n")

if __name__ == "__main__":
    main()