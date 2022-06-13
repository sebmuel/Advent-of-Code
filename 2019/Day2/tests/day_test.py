import unittest

from Day2.BoardComputer import CodePart1, CodePart2


class CodeFactory:

    @staticmethod
    def get_insert_list(int_codes: [int]):
        code = CodePart1(int_codes)
        code.eval_code()
        return code.int_codes


class TestIntCode(unittest.TestCase):
    def test_eval(self):
        self.assertEqual(CodeFactory.get_insert_list([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
        self.assertEqual(CodeFactory.get_insert_list([2, 3, 0, 3, 99]), [2, 3, 0, 6, 99])
        self.assertEqual(CodeFactory.get_insert_list([2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(CodeFactory.get_insert_list([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == '__main__':
    unittest.main()
