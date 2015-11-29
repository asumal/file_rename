__author__ = 'Arjun'

import unittest
import os

TEST_FILE_NAME = "test.png"


from file_rename.file_rename import (ListOfFiles)


class TestFileRename(unittest.TestCase):
    def setUp(self):
        path_to_files = os.path.join(os.getcwd(), "data")
        self.list_of_files = ListOfFiles(path_to_files)

    def test_storing_files(self):
        change_file_names = self.list_of_files
        assert TEST_FILE_NAME in change_file_names.files

    def test_num_files(self):
        change_file_names = self.list_of_files
        assert change_file_names.num_files == 1



if __name__ == "__main__":
    unittest.main()
