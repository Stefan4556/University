import unittest
from utils.utils import generate_apples, adjacent


class TesteUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_adjacent(self):
        self.assertTrue(adjacent([1, 2], [1, 3]))
        self.assertFalse(adjacent([1, 2], [1, 4]))
        self.assertTrue(adjacent([1, 3], [2, 3]))
        self.assertFalse(adjacent([1, 3], [3, 3]))

    def test_generate_apples(self):
        head = [2, 3]
        tail = [[3, 3], [3, 4]]
        list_apples = generate_apples(head, tail, 10, 7)
        self.assertEqual(len(list_apples), 10)