import unittest
from algorithm import replace_list

class TestReplace(unittest.TestCase):
    def setUp(self):
        self.array = [10, 5, 20, 30, 5, 4]

    def test_existing(self):
        self.assertListEqual([10,5,5,30,5,4], replace_list(self.array, 20, 5))

    def test_existingMultiple(self):
        self.assertListEqual([10,7,20,30,7,4], replace_list(self.array, 5, 7))

    def test_nonexisting(self):
        self.assertListEqual([10,5,20,30,5,4], replace_list(self.array, 3, 6))

    def test_emptyArray(self):
        self.assertListEqual([], replace_list([], 3, 6))

    def test_wrongParamType1(self):
        self.assertFalse(replace_list('a', 3, 6))

    def test_wrongParamType2(self):
        self.assertFalse(replace_list([10, 5, 20, 30, 5, 4], '3', 6))

    def test_wrongParamType3(self):
        self.assertFalse(replace_list([10, 5, 20, 30, 5, 4], 3, '6'))

if __name__ == '__main__':
    unittest.main()
