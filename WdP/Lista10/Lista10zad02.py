class Employee:
    """Class representing a single employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_value=2000):
        """Increases the annual salary by a given value"""
        self.annual_salary += raise_value
