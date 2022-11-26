import numpy
from scipy import linalg
import unittest


class TestMatrixLUDecomposition(unittest.TestCase):
    def setUp(self):
        self.sample_matrix = numpy.array([[7, 3, -1, -2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]])
        self.p, self.l, self.u = linalg.lu(self.sample_matrix)

    def test_int(self):
        for i in range(len(self.sample_matrix)):
            for j in range(len(self.sample_matrix[i])):
                self.assertIsInstance(self.sample_matrix[i][j], numpy.int32)

    def test_matrix(self):
        """Makes sure, that the given object is indeed a matrix"""
        columns_ex = len(self.sample_matrix[0])
        for i in self.sample_matrix:
            columns = len(i)
            self.assertEqual(columns, columns_ex)

    def test_shape(self):
        """Checks whether the given matrix is square"""
        rows = len(self.sample_matrix)
        for i in self.sample_matrix:
            columns = len(i)
            self.assertEqual(columns, rows)

            # Alternatively

        self.assertEqual(numpy.shape(self.sample_matrix)[0], numpy.shape(self.sample_matrix)[1])

    def test_determinant(self):
        """Rejects the matrix if it's determinant is equal to 0"""
        self.assertNotEqual(linalg.det(self.sample_matrix), 0)

    def test_lower(self):
        """Searches for zeros over the diagonal to make sure we're dealing with a lower triangular matrix"""
        temp = 1
        for i in range(len(self.l)):
            for j in range(temp, len(self.l)):
                self.assertEqual(self.l[i][j], 0)
            temp += 1

    def test_L(self):
        """Evaluates the lower matrix"""
        self.assertTrue(
            (self.l == [[1, 0, 0, 0],
                        [3 / 7, 1, 0, 0],
                        [-1 / 7, 10 / 47, 1, 0],
                        [2 / 7, -34 / 47, 15 / 167, 1]]).all)

    def test_upper(self):
        """Searches for zeros under the diagonal to make sure we're dealing with a lower triangular matrix"""
        temp = 0
        for i in range(len(self.u)):
            for j in range(temp):
                self.assertEqual(self.u[i][j], 0)
            temp += 1

    def test_U(self):
        """Evaluates the upper matrix"""
        self.assertTrue((self.u == [[7, 3, -1, 2],
                                    [0, 47/7, 10/7, -34/7],
                                    [0, 0, 167/47, 15/47],
                                    [0, 0, 0, 315/167]]).all)

    def test_P(self):
        """I'm not sure if this is even necessary, but at this point why not"""
        self.assertTrue((self.p == [[1, 0, 0, 0],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]]).all)


if __name__ == "__main__":
    unittest.main()
