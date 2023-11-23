import unittest

from main import paginate


class TestPagination(unittest.TestCase):

    def test_valid_pagination(self):
        result = paginate(4, 10, 2, 2)
        self.assertEqual(result, "1 2 3 4 5 6 ... 9 10")

    def test_pagination_with_around_equals_zero(self):
        result = paginate(4, 5, 1, 0)
        self.assertEqual(result, "1 ... 4 5")

    def test_curent_page_in_the_middle_of_all_pages(self):
        result = paginate(50, 100, 2, 2)
        self.assertEqual(result, "1 2 ... 48 49 50 51 52 ... 99 100")

    def test_zero_total_pages(self):
        with self.assertRaises(ValueError):
            paginate(1, 0, 2, 2)

    def test_negative_current_pages_value(self):
        with self.assertRaises(ValueError):
            paginate(-1, 10, 2, 2)

    def test_negative_total_pages_value(self):
        with self.assertRaises(ValueError):
            paginate(1, -1, 2, 2)

    def test_negative_boundaries_value(self):
        with self.assertRaises(ValueError):
            paginate(1, 1, -1, 2)

    def test_negative_around_value(self):
        with self.assertRaises(ValueError):
            paginate(1, 1, 1, -1)

    def test_current_page_is_greater_than_total_pages(self):
        with self.assertRaises(ValueError):
            paginate(15, 10, 2, 2)

    def test_current_page_is_less_than_total_pages(self):
        with self.assertRaises(ValueError):
            paginate(0, 10, 2, 2)

    def test_invalid_type_of_current_page_argument(self):
        with self.assertRaises(TypeError):
            paginate("1", 10, 2, 2)
    def test_invalid_type_of_total_pages_argument(self):
        with self.assertRaises(TypeError):
            paginate(1, "10", 2, 2)
    def test_invalid_type_of_boundaries_argument(self):
        with self.assertRaises(TypeError):
            paginate(1, 10, "2", 2)
    def test_invalid_type_of_around_argument(self):
        with self.assertRaises(TypeError):
            paginate(1, 10, 2, "2")

    def test_pagination_with_one_page(self):
        result = paginate(1, 1, 1, 0)
        self.assertEqual(result, "1")

    def test_pagination_with_no_boundaries(self):
        result = paginate(3, 10, 0, 0)
        self.assertEqual(result, "1 ... 3 ... 10")

    def test_pagination_with_boundaries_is_greater_than_total_pages(self):
        result = paginate(3, 10, 10000, 0)
        self.assertEqual(result, "1 2 3 4 5 6 7 8 9 10")

    def test_pagination_with_boundaries_equal_total_pages(self):
        result = paginate(5, 5, 5, 0)
        self.assertEqual(result, "1 2 3 4 5")

    def test_pagination_with_around_completely_inside_left_boundary(self):
        result = paginate(10, 10, 3, 1)
        self.assertEqual(result, "1 2 3 ... 8 9 10")

    def test_pagination_with_around_completely_inside_right_boundary(self):
        result = paginate(2, 10, 3, 1)
        self.assertEqual(result, "1 2 3 ... 8 9 10")

    def test_pagination_with_current_page_on_last_page(self):
        result = paginate(10, 10, 2, 2)
        self.assertEqual(result, "1 2 ... 8 9 10")

    def test_pagination_with_current_page_on_first_page(self):
        result = paginate(1, 10, 2, 1)
        self.assertEqual(result, "1 2 ... 9 10")


if __name__ == "__main__":
    unittest.main()
