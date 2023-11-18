import unittest

from main import paginate


class TestPagination(unittest.TestCase):

    def test_valid_pagination(self):
        result = paginate(4, 10, 2, 2)
        self.assertEqual(result, "1 2 3 4 5 6 ... 9 10")

    def test_curent_page_in_the_middle_of_all_pages(self):
        result = paginate(50, 100, 2, 2)
        self.assertEqual(result, "1 2 ... 48 49 50 51 52 ... 99 100")

    def test_zero_total_pages(self):
        with self.assertRaises(ValueError):
            paginate(1, 0, 2, 2)

    def test_negative_values(self):
        values_list = [
            [-1, 10, 2, 2],
            [1, -10, 2, 2],
            [1, 10, -2, 2],
            [1, 10, 2, -2]
        ]
        with self.assertRaises(ValueError):
            for values in values_list:
                paginate(*values)

    def test_current_page_out_of_range(self):
        with self.assertRaises(ValueError):
            paginate(15, 10, 2, 2)

        with self.assertRaises(ValueError):
            paginate(0, 10, 2, 2)

    def test_invalid_argument_types(self):
        with self.assertRaises(TypeError):
            paginate('1', 10, 2, 2)

        with self.assertRaises(TypeError):
            paginate(1, 10, 2, '2')

    def test_pagination_with_one_page(self):
        result = paginate(1, 1, 1, 0)
        self.assertEqual(result, "1")

    def test_pagination_with_no_boundaries(self):
        with self.assertRaises(ValueError):
            paginate(1, 1, 0, 1)


if __name__ == "__main__":
    unittest.main()
