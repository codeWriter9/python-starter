# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from hello.helloWorld import hello_world


class TestSimple(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World!!")


if __name__ == '__main__':
    unittest.main()
