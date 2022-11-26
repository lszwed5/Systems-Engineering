import unittest
from Lista10zad02 import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the Employee class"""
    def setUp(self):
        self.employee1 = Employee("John", "Smith", 2000)

    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, 4000)

    def test_give_custom_raise(self):
        self.employee1.give_raise(3000)
        self.assertEqual(self.employee1.annual_salary, 5000)


if __name__ == "__main__":
    unittest.main()
