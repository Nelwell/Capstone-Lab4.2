'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''

import unittest

from studentlists import ClassList, StudentError
from unittest import TestCase


class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):  # expects a student error when next line runs
            test_class.add_student('Test Student')

    # adds and removes a student, and asserts the student is removed.
    # Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    # test that adds some example students,
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_remove_student_not_in_the_list_raises_student_error(self):
        # Arrange
        test_class = ClassList(4)
        test_class.add_student('Alice')
        test_class.add_student('Bob')

        # remove 'Carl', expect a StudentError
        # Assert
        with self.assertRaises(StudentError):  # expects a student error when next line runs
            # Action
            test_class.remove_student('Carl')

    # removes a student from an empty list, and asserts a StudentError is raised
    def test_remove_student_from_empty_class_list_raises_student_error(self):
        # empty class, no students added
        # Arrange
        test_class = ClassList(3)

        # remove 'Carl', expect a StudentError
        # Assert
        with self.assertRaises(StudentError):  # expects a student error when next line runs
            # Action
            test_class.remove_student('Carl')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    # adds some example students to a test class,
    # then, call is_enrolled for a student who is not enrolled.
    # Use assertFalse to verify is_enrolled returns False.
    def test_student_not_in_class_is_not_enrolled(self):
        # Arrange
        test_class = ClassList(3)  # example class with max 3 students
        test_class.add_student('Alice')
        test_class.add_student('Bob')

        # carl is not registered
        # Action
        is_carl_enrolled = test_class.is_enrolled('Carl')

        # Assert
        self.assertFalse(is_carl_enrolled)

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    # test for index_of_student when the class_list list is empty.
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
    def test_index_of_student_student_list_empty(self):
        # empty class, no students added
        # Arrange
        test_class = ClassList(3)

        # Assert/Action
        self.assertIsNone(test_class.index_of_student('Carl'))  # expects None value for list

    # test for index_of_student. In the case when the
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_student_not_present(self):
        test_class = ClassList(6)
        test_class.add_student('Cloud')
        test_class.add_student('Squall')
        test_class.add_student('Zell')

        self.assertEqual(1, test_class.index_of_student('Cloud'))
        self.assertEqual(2, test_class.index_of_student('Squall'))
        self.assertEqual(3, test_class.index_of_student('Zell'))

        # will pass if the method call returns None
        self.assertIsNone(test_class.index_of_student('Cid'))

    # test for your new is_class_full method when the class is full.
    # use assertTrue.
    def test_is_class_full_class_is_full(self):
        # fill up class with students
        test_class = ClassList(3)
        test_class.add_student('Cloud')
        test_class.add_student('Squall')
        test_class.add_student('Zell')

        # will pass if class is full
        self.assertTrue(test_class.is_class_full())

    # test for your new is_class_full method for when is empty,
    # and when it is not full. Use assertFalse.
    def test_is_class_empty_or_not_full(self):
        # empty class
        empty_test_class = ClassList(3)
        # add students
        test_class = ClassList(4)
        test_class.add_student('Cloud')
        test_class.add_student('Squall')
        test_class.add_student('Zell')

        # will pass if class is not full or is empty
        self.assertFalse(empty_test_class.is_class_full())
        self.assertFalse(test_class.is_class_full())

    def test_max_students_is_zero_or_negative(self):
        # checks if StudentError is raised for zero or negative max_students value
        with self.assertRaises(StudentError):
            ClassList(0)
        with self.assertRaises(StudentError):
            ClassList(-3)


if __name__ == '__main__':
    # allows right-click running of test
    unittest.main()
