import unittest


class TestUnittestDemo(unittest.TestCase):

    def test_demo1(self):
        self.assertTrue(True, "test true")


if __name__ == '__main__':
    unittest.main()