class Student(object):
    """
    A Student represents a certain student

    """
    def __init__(self, student_id, courses):
        """
        Initializes a student with courses

        """
        self.student_id = student_id
        self.courses = courses

    def numberCourses(self):
        """
        returns number of courses

        """
        return len(self.courses)

class Course(object):
    """
    A Course represents a certain course.
    """
    def __init__(self, name, students):
        """
        Initializes a course with students

        """
        self.name = name
        self.students = students

    def numberStudents(self):
        """
        returns number of students

        """
        return len(self.students)


def main():
    '''
    Extracts data from original CSV file (studenten_roostering).

    Outputs lists: student_list and course_list, which are lists of objects
    '''
    import csv
    import random

    # open csv file and reads into csv-file
    f = open('studenten_roostering.csv')
    csv_file = csv.reader(f)

    # empty list for student and course objects
    student_list = []
    course_list = []
    student_infos = []

    # extracts the id and courses of every student
    for csv_line in csv_file:
        student_infos.append(csv_line)

    for student_info in student_infos[1:10]:
        student_id = student_info[2]
        courses_student = []
        for student_course in student_info[3:]:
            if student_course != "":
                courses_student.append(student_course)


        # [course for course in ["vak1", "vak2", "", ""] if course]
        # create new student object and adds it to list
        student = Student(student_id, courses_student)

        student_list.append(student)

        # loops over courses of the student
        for course_student in courses_student:
            course_exists = False
            # checks if course already exists
            for course in course_list:
                if course.name == course_student:
                    course.students.append(student_id)
                    course_exists = True
            if course_exists == False:
                if course_student != '':
                    # creates new course object w
                    students = []
                    course = Course(course_student, students)
                    course_list.append(course)
                    course.students.append(student_id)

    # returns list of student objects and list of course objects
    return [student_list, course_list]
