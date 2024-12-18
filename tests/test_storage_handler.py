import unittest
from unittest.mock import patch, mock_open

from src.storage_handler import read_from_file, write_rows_to_file, write_row_to_file


class TestStorageHandler(unittest.TestCase):

    def test_read_from_file(self):
        open_mock = mock_open()
        with patch("builtins.open", mock_open(read_data="1,Adam,Nowak")):
            result = read_from_file("path")
            self.assertEqual(result, [["1", "Adam", "Nowak"]])


    def test_write_row_to_file(self):
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=True):
            write_row_to_file("path", [0, "Adam", "Nowak"])
        
        open_mock.assert_called_with("path", "w")
        open_mock.return_value.write.assert_called_once_with("0,Adam,Nowak\r\n")