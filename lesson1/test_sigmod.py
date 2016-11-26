import unittest
from sigmod.sigmod_handle import sigmod

class MyTestCase(unittest.TestCase):

    def test_something(self):
        x = -9999999.0
        self.assertAlmostEqual(0, sigmod(x), 7, "negative infinity, test failed.", None)
        x = 0.0
        self.assertAlmostEqual(0.5, sigmod(x), 7, "zero, test failed.", None)
        x = 99999999.0
        self.assertAlmostEqual(1, sigmod(x), 7, "positive infinity, test failed.", None)
        print "test pass"

#        places = 0.00000001
#        self.assertAlmostEqual(0, places, 7, "failed", None)


if __name__ == '__main__':
    unittest.main()
