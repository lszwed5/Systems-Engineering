# Dorysować histogram
import numpy
from matplotlib import pyplot as plt
import numpy as np
import random


class GradeArray:
    """Class representing a single grade array"""

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.array = np.zeros((self.m, self.n))
        for student in range(self.m):
            for course in range(self.n):
                self.array[student][course] = random.choice((2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5))

    def not_passed(self, n):
        """Shows how many students have failed in at least n given courses"""
        number_of_students = 0
        for student in range(self.m):
            number_of_courses = 0
            for course in range(self.n):
                if self.array[student][course] < 3.0:
                    number_of_courses += 1
            if number_of_courses >= n:
                number_of_students += 1
        print(f"Liczba studentów, którzy nie zaliczyli co najmniej {n} przedmiotów wynosi {number_of_students}")
        print()

    def extremum_grades(self):
        """Shows the grade average of the worst and best student(s)"""
        averages = []
        for student in range(self.m):
            averages.append(sum(self.array[student]) / len(self.array[student]))
        print("Oceny studenta (studentów) z najniższą średnią to:")
        for student in range(self.m):
            if averages[student] == min(averages):
                print(self.array[student])
        print()
        print("Oceny studenta (studentów) z najwyższą średnią to:")
        for student in range(self.m):
            if averages[student] == max(averages):
                print(self.array[student])
        print()

    def most_highest(self):
        """Shows the ID of the student, who got the highest number of the highest grades in a given array"""
        student_num_of_max = []
        for student in range(self.m):
            number_of_max = 0
            for course in range(self.n):
                if self.array[student][course] == numpy.amax(self.array):
                    number_of_max += 1
            student_num_of_max.append(number_of_max)
        print(f"Student (studenci) z najwyższą ({max(student_num_of_max)}) "
              f"liczbą ocen najwyższych ({numpy.amax(self.array)}), to student (studenci): ")
        for student in range(self.m):
            if student_num_of_max[student] == max(student_num_of_max):
                print(student)
                # print(student + 1)
        print()

    def histogram(self):
        pass

    def high_averages(self):
        """Shows the list of the students with grade average greater or equal to 4.5"""
        best_students = 0
        print("Studenci ze średnią powyżej 4.5 to: ")
        for student in range(self.m):
            if sum(self.array[student]) / len(self.array[student]) >= 4.5:
                best_students += 1
                print(student)
                # print(student + 1)
        if best_students == 0:
            print("Niestety w tej tabeli nie ma takich studentów!")
        print()


grade_array = GradeArray(5, 5)
print(grade_array.array)
print()
print("---------------------------------------------------------------------------------------------\n")
grade_array.not_passed(2)
print("---------------------------------------------------------------------------------------------\n")
grade_array.extremum_grades()
print("---------------------------------------------------------------------------------------------\n")
grade_array.most_highest()
print("---------------------------------------------------------------------------------------------\n")
grade_array.high_averages()
