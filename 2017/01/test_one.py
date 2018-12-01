import unittest
from one import captcha_solver


class TestCaptchaSolver(unittest.TestCase):
    def test_captcha_solver_1(self) -> None:
        result = captcha_solver("1122")
        self.assertEqual(result, 3)

    def test_captcha_solver_2(self) -> None:
        result = captcha_solver("1111")
        self.assertEqual(result, 4)

    def test_captcha_solver_3(self) -> None:
        result = captcha_solver("1234")
        self.assertEqual(result, 0)

    def test_captcha_solver_4(self) -> None:
        result = captcha_solver("91212129")
        self.assertEqual(result, 9)

    def test_captcha_solver_5(self) -> None:
        result = captcha_solver("11112")
        self.assertEqual(result, 3)
