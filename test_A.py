from __future__ import absolute_import, division, print_function, unicode_literals

import A
import unittest


class TestA(unittest.TestCase):
    def test_call_B_from_A(self):
        A.B()
        # try to test if something printed, find three things printed

    def test_import_B(self):
        import B

    def test_import_C(self):
        import B.C

if __name__ == '__main__':
    unittest.main()
