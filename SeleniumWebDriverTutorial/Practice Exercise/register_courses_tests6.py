from register_courses_page6 import RegisterCoursesPage
from Automation_Framework_3.teststatus5 import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="1234 5678 9012 3456", exp="1220", cvv="444", zip="12345")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")