import unittest
import numpy as np

from QGen.Fingerprint import Fingerprint

class TestFingerprint(unittest.TestCase):

    def test_basic(self):
        fp = Fingerprint([1] * 50)
        np.testing.assert_array_equal(fp.value, np.array([1] * 50))

    def test_wrong_size_fail(self):
        with self.assertRaises(Exception):
            Fingerprint([1] * 49)

    def test_building_from_list(self):
        zero_fp = Fingerprint([0] * 50)
        one_fp = Fingerprint([1] * 50)
        result_fp = Fingerprint(fingerprint_list=[zero_fp, one_fp])
        np.testing.assert_array_equal(result_fp.value, np.array([0.5] * 50))

if __name__ == '__main__':
    unittest.main()
