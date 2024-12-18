from src.storage_handler import write_rows_to_file

class StudentHandler:
    def __init__(self, list_of_students = [], file_path: str = "data/students.csv"):
        self.list_of_students = []
        if list_of_students is not None:
            for student in list_of_students:
                self.list_of_students.append([int(student[0]), student[1], student[2]])

        self.file_path = file_path


    # returning student when exist
    def get_student(self, id: int):
        for student in self.list_of_students:
            if student[0] == id:
                return student
        return None
    
    
    def generate_id(self):
        if len(self.list_of_students) == 0:
            return 1
        return self.list_of_students[-1][0] + 1


    def add_student(self, id: int, first_name: str, surname: str):
        self.list_of_students.append([id, first_name.title(), surname.title()])
        write_rows_to_file(path=self.file_path, data=self.list_of_students)


    def remove_student(self, id: int):
        self.list_of_students.remove(self.get_student(id))
        write_rows_to_file(path=self.file_path, data=self.list_of_students)

