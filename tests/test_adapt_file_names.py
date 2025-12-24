import unittest
from unittest.mock import patch

from unittest_parametrize import parametrize, ParametrizedTestCase

from adapt_file_names import adapt_mp4_file_name, adapt_png_file_name


class TestAdaptMP4FileNames(ParametrizedTestCase, unittest.TestCase):

    def setUp(self):
        self.print_patcher = patch('adapt_file_names.print')
        self.mock_print = self.print_patcher.start()

    def tearDown(self):
        self.print_patcher.stop()

    @parametrize(
        "input_file_name, expected_file_name",
        [
            ("Cool Game 2023.08.15.mp4", "Cool_Game_2023-08-15.mp4"),
            ("Another Game 2022.12.01_extra_info.mp4", "Another_Game_2022-12-01_extra_info.mp4"),
            ("The Game 2023.08.15 - 12.64.12.75.DVR.mp4", "The_Game_2023-08-15.mp4"),
            ("The Game 2023.08.15_extra_Info - 12.64.12.75.DVR.mp4", "The_Game_2023-08-15_extra_Info.mp4"),
        ],
    )
    def test__should_adapt_mp4_file_name(self, input_file_name, expected_file_name):
        with patch('adapt_file_names.config', {'ENABLE_REPLACEMENT_NAMES': False}):
            result_file_name = adapt_mp4_file_name(input_file_name)

        self.assertEqual(expected_file_name, result_file_name)

    @parametrize(
        "input_file_name",
        [
            "Another_Game_2022-12-01_extra_info.mp4",
            "Another Game 22.12.1.mp4",
            "InvalidFileName.mp4",
        ],
    )
    def test__should_return_None_on_false_structure(self, input_file_name):
        with patch('adapt_file_names.config', {'ENABLE_REPLACEMENT_NAMES': False}):
            result_file_name = adapt_mp4_file_name(input_file_name)

        self.assertEqual(None, result_file_name)


    def test__should_adapt_mp4_file_name_with_replacement(self):
        input_file_name = "Cool Game 2023.08.15.mp4"

        with patch('adapt_file_names.config', {'ENABLE_REPLACEMENT_NAMES': True}), \
             patch('adapt_file_names.known_games', {'Cool Game': 'Awesome Game'}):
            result_file_name = adapt_mp4_file_name(input_file_name)

        expected_file_name = "Awesome_Game_2023-08-15.mp4"

        self.assertEqual(expected_file_name, result_file_name)


class TestAdaptPNGFileNames(ParametrizedTestCase, unittest.TestCase):

    def setUp(self):
        # Patch print um Ausgaben zu unterdrücken
        self.print_patcher = patch('adapt_file_names.print')
        self.mock_print = self.print_patcher.start()

    def tearDown(self):
        self.print_patcher.stop()

    @parametrize(
        "input_file_name, expected_file_name",
        [
            ("Cool Game Screenshot 2023.08.15.png", "Cool_Game_Screenshot_2023-08-15.png"),
            ("Another Game Screenshot 2022.12.01_extra_info.png", "Another_Game_Screenshot_2022-12-01_extra_info.png"),
        ],
    )
    def test__should_adapt_png_file_name(self, input_file_name, expected_file_name):
        with patch('adapt_file_names.config', {'ENABLE_REPLACEMENT_NAMES': False}):
            result_file_name = adapt_png_file_name(input_file_name)

        self.assertEqual(expected_file_name, result_file_name)

    @parametrize(
        "input_file_name",
        [
            "Another_Game_Screenshot_2022-12-01_extra_info.png",
            "Another Game 2022.12.01.png",
            "InvalidFileName.png",
        ],
    )
    def test__should_return_None_on_false_structure(self, input_file_name):
        with patch('adapt_file_names.config', {'ENABLE_REPLACEMENT_NAMES': False}):
            result_file_name = adapt_png_file_name(input_file_name)

        self.assertEqual(None, result_file_name)


    def test__should_adapt_png_file_name_with_replacement(self):
        input_file_name = "Cool Game Screenshot 2023.08.15.png"

        with patch('adapt_file_names.config', {'ENABLE_REPLACEMENT_NAMES': True}), \
             patch('adapt_file_names.known_games', {'Cool Game': 'Awesome Game'}):
            result_file_name = adapt_png_file_name(input_file_name)

        expected_file_name = "Awesome_Game_Screenshot_2023-08-15.png"

        self.assertEqual(expected_file_name, result_file_name)

if __name__ == "__main__":
    unittest.main()
