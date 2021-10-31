"""Multiple Choice Tests

Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper and
to be also able to assign a minimum pass mark. The testpaper's subject should also be included. The attributes are in
the following order:

    subject
    markscheme
    pass_mark

As well as that, we need to create student objects to take the test itself! Create another class called Student and do
the following:

    Create an attribute called tests_taken and set the default as 'No tests taken'.
    Make a method called take_test(), which takes in the testpaper object they are completing and the student's answers.
    Compare what they wrote to the mark scheme, and append to the/create a dictionary assigned to tests_taken in the
    way as shown in the point below.
    Each key in the dictionary should be the testpaper subject and each value should be a string in the format seen in
    the examples below (whether or not the student has failed, and their percentage in brackets).

Examples

paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()

student1.tests_taken ➞ "No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

Notes

    Round percentages to the nearest whole number.
    Remember that the attribute tests_taken should return 'No tests taken' when no tests have been taken yet.
"""
from typing import Union


class Testpaper:
    def __init__(self, subject: str, mark_scheme: list[str], pass_mark: str):
        self.subject: str = subject
        self.mark_scheme: list[str] = mark_scheme
        self.pass_mark: str = pass_mark


class Student:
    def __init__(self):
        self._tests_taken = 'No tests taken'

    @property
    def tests_taken(self) -> Union[str, dict]:
        return self._tests_taken

    def take_test(self, testpaper: Testpaper, answers: list[str]) -> None:
        student_mark = self._get_mark(testpaper.mark_scheme, answers)
        pass_mark = int(testpaper.pass_mark.replace('%', ''))

        if student_mark >= pass_mark:
            res = {testpaper.subject: 'Passed! ({}%)'.format(student_mark)}
        else:
            res = {testpaper.subject: 'Failed! ({}%)'.format(student_mark)}

        if isinstance(self._tests_taken, str):
            self._tests_taken = res
        elif isinstance(self._tests_taken, dict):
            self._tests_taken.update(res)

    @staticmethod
    def _get_mark(real_answers: list, student_answers: list) -> int:
        correct = 0
        for answers in zip(real_answers, student_answers):
            real, student = answers
            if real == student:
                correct += 1

        return int(round((correct / len(real_answers)) * 100))


if __name__ == '__main__':
    paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

    student1 = Student()
    student2 = Student()

    assert student1.tests_taken == "No tests taken"
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    assert student1.tests_taken == {"Maths": "Passed! (80%)"}

    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    assert student2.tests_taken == {"Chemistry": "Failed! (25%)", "Computing": "Failed! (43%)"}
