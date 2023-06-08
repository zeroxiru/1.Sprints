import unittest
import parse_classroom


class TestReadFile(unittest.TestCase):
    def test_structure(self):
        # Set the expected return value
        expected = [{'name': 'Ron', 'country': 'Germany', 'grades': [100, 90, 81]},
                    {'name': 'Jonathan', 'country': 'United States', 'grades': [85, 45, 66]},
                    {'name': 'Griffin', 'country': 'United Kingdom', 'grades': [100, 90, 95]},
                    {'name': 'Daniel', 'country': 'United States', 'grades': [100, 99, 77]}]

        # Get the actual return value of the student's function
        actual = parse_classroom.parse_simple_classroom(parse_classroom.SIMPLE_CLASSROOM_PATH)

        # Check that it equal
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
