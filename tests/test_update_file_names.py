import os
import unittest
from unittest.mock import patch

from unittest_parametrize import ParametrizedTestCase, parametrize

from update_file_names import update_file_names, __get_new_file_name


class TestUpdateFileNames(ParametrizedTestCase, unittest.TestCase):

    def test__should_update_files_correctly(self):
        with patch("os.rename") as mock_rename, \
             patch("os.walk") as mock_walk:
            mock_walk.return_value = [
                ("/path/coolGame/Cutted", [], ["Cool Game 2023.08.15.mp4", "Cool Game Screenshot 2023.08.15.png"]),
                ("/path/anotherGame/Cutted", [], ["Another Game 2022.12.01_extra_info.mp4", "Another Game Screenshot 2022.12.01_extra_info.png"]),
            ]

            update_file_names("/path")

            expected_calls = [
                (os.path.join("/path/coolGame/Cutted", "Cool Game 2023.08.15.mp4"),
                 os.path.join("/path/coolGame/Cutted", "Cool_Game_2023-08-15.mp4")),
                (os.path.join("/path/coolGame/Cutted", "Cool Game Screenshot 2023.08.15.png"),
                 os.path.join("/path/coolGame/Cutted", "Cool_Game_Screenshot_2023-08-15.png")),
                (os.path.join("/path/anotherGame/Cutted", "Another Game 2022.12.01_extra_info.mp4"),
                 os.path.join("/path/anotherGame/Cutted", "Another_Game_2022-12-01_extra_info.mp4")),
                (os.path.join("/path/anotherGame/Cutted", "Another Game Screenshot 2022.12.01_extra_info.png"),
                 os.path.join("/path/anotherGame/Cutted", "Another_Game_Screenshot_2022-12-01_extra_info.png")),
            ]

            actual_calls = [call.args for call in mock_rename.call_args_list]

            self.assertEqual(expected_calls, actual_calls)

    def test__should_not_update_adapted_or_false_files(self):
        with patch("os.rename") as mock_rename, \
             patch("os.walk") as mock_walk:
            mock_walk.return_value = [
                ("/path/coolGame/Cutted", [], ["Cool_Game_2023-08-15.mp4", "Cool_Game_Screenshot_2023-08-15.png", "Cool_Game_23-8-15.mp4"]),
            ]

            update_file_names("/path")

            expected_calls = []

            actual_calls = [call.args for call in mock_rename.call_args_list]

            self.assertEqual(expected_calls, actual_calls)

if __name__ == "__main__":
    unittest.main()