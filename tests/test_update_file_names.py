import unittest
from unittest.mock import patch

from unittest_parametrize import ParametrizedTestCase

from update_file_names import update_file_names

@patch('update_file_names.print')
class TestUpdateFileNames(ParametrizedTestCase, unittest.TestCase):

    def test__should_update_files(self, _mock_print):
        with patch("os.rename") as mock_rename, \
             patch("os.walk") as mock_walk, \
             patch("update_file_names.__get_new_file_name") as mock_get_new_file_name:
            mock_walk.return_value = [
                ("/path/coolGame/Cutted", [], ["file1", "file2", "file3"]),
                ("/path/anotherGame/Cutted", [], ["file1", "file2"]),
                ("/path/theGame/Cutted", [], ["file1"]),
            ]

            mock_get_new_file_name.return_value = "adapted_file_name"

            update_file_names("/path")

            actual_calls = len(mock_rename.call_args_list)

            self.assertEqual(6, actual_calls)

    def test__should_not_update_files(self, _mock_print):
        with patch("os.rename") as mock_rename, \
             patch("os.walk") as mock_walk, \
             patch("update_file_names.__get_new_file_name") as mock_get_new_file_name:
            mock_walk.return_value = [
                ("/path/coolGame/Cutted", [], ["file1", "file2", "file3"]),
            ]

            mock_get_new_file_name.return_value = None

            update_file_names("/path")

            actual_calls = len(mock_rename.call_args_list)

            self.assertEqual(0, actual_calls)

    def test__should_skip_non_cutted_directories(self, _mock_print):
        with patch("os.rename") as mock_rename, \
             patch("os.walk") as mock_walk, \
             patch("update_file_names.__get_new_file_name") as mock_get_new_file_name:
            mock_walk.return_value = [
                ("/path/coolGame", [], ["file1", "file2", "file3"]),
            ]

            mock_get_new_file_name.return_value = "adapted_file_name"

            update_file_names("/path")

            actual_calls = len(mock_rename.call_args_list)

            self.assertEqual(0, actual_calls)

if __name__ == "__main__":
    unittest.main()