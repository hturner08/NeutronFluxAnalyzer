import unittest

class TestStringMethods(unittest.TestCase):

    def test_resize(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_blend(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
#
