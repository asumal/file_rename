__author__ = 'Arjun'

import unittest
import os

from file_rename.file_rename import (ListOfFiles)


class TestFileRename(unittest.TestCase):
    def setUp(self):
        path_to_files = os.path.join(os.getcwd(), "data")
        print path_to_files
        self.list_of_files = ListOfFiles(path_to_files)

    def test_retrieval_of_files(self):
        assert len(self.list_of_files.path_to_files) == 1

if __name__ == "__main__":
    unittest.main()
