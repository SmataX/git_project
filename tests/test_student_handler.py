import unittest
from unittest.mock import patch, mock_open

from src.student_handler import StudentHandler


class TestStudentHandler(unittest.TestCase):
    def test_get_student(self):
        student_handler = StudentHandler([[1, "Adam", "Nowak"], [2, "Jan", "Kowalski"], [3, "Michał", "Mróz"]])
        self.assertEqual(student_handler.get_student(2), [2, "Jan", "Kowalski"])


    def test_generate_id(self):
        student_handler = StudentHandler([[1, "Adam", "Nowak"], [2, "Jan", "Kowalski"], [3, "Michał", "Mróz"]])
        self.assertEqual(student_handler.generate_id(), 4)


    def test_add_student(self):
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=True):
            student_handler = StudentHandler()
            student_handler.add_student(0, "Adam", "Nowak")
        
            self.assertEqual(len(student_handler.list_of_students), 1)
            self.assertEqual(student_handler.list_of_students[0], [0, "Adam", "Nowak"])


    def test_remove_student(self):
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=True):
            student_handler = StudentHandler([[1, "Adam", "Nowak"], [2, "Jan", "Kowalski"], [3, "Michał", "Mróz"]])
            student_handler.remove_student(2)
        
            self.assertEqual(len(student_handler.list_of_students), 2)
            self.assertEqual(student_handler.list_of_students[0], [1, "Adam", "Nowak"])
            self.assertEqual(student_handler.list_of_students[1], [3, "Michał", "Mróz"])