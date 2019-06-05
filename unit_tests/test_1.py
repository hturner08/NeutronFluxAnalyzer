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
# ranges = [.3, .5, .7]
# blended = []
# for x in ranges:
#     blended.append(combine_images(graph, diagram,300,700,x))
# for img in blended:
#     cv.imshow('test',img)
#     cv.waitKey(3000)
