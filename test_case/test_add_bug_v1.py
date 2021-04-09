import unittest

from config.public_login import Login


class MyTestCase(unittest.TestCase):

    def setUp(self):
        Login.test_login_success()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
