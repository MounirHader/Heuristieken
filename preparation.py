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
        self.sessions =

    def numberStudents(self):
        """
        returns number of students

        """
        return len(self.students)

class Session(object):
    """
    A Session represents a certain session of a course.
    """
    def __init__(self, session_type, course, students):
        """
        Initializes a session with students

        """
        self.session_type = session_type
        self.course = course
        self.students = students

    def numberStudents(self):
        """
        returns number of students

        """
        return len(self.students)

class Room(object):
    """
    A Room represents a certain room.
    """
    def __init__(self, name, capacity):
        """
        Initializes a session with students

        """
        self.name= name
        self.capacity = capacity


def main():
    '''
    Extracts data from original CSV file (studenten_roostering).

    Outputs lists: student_list and course_list, which are lists of objects
    '''
    import csv
    import random

    # open csv files and reads into csv-file
    f1 = open('studenten_roostering.csv')
    csv_file_1 = csv.reader(f1)
    f2 = open('vak_specificaties.csv')
    csv_file_2 = csv.reader(f2, delimiter=';')

    # empty list for student and course objects
    student_list = []
    course_list = []
    student_infos = []

    # extracts the id and courses of every student
    for csv_line in csv_file_1:
        student_infos.append(csv_line)

    for student_info in student_infos[1:10]:
        student_id = student_info[2]
        courses_student = []
        for student_course in student_info[3:]:
            if student_course != "":
                courses_student.append(student_course)


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

    # extracts the specifications of every course
    course_specifications = []
    for csv_line in csv_file_2:
        course_specifications.append(csv_line)

    session_list = []

    # creates different session objects for every course object
    for course in course_list:
        course_sessions = []
        num_students = course.numberStudents()
        for course_specification in course_specifications:
            if course.name == course_specification[0]:
                # creates lectures
                num_lectures = int(course_specification[1])
                for i in range(num_lectures):
                    session_type = "lecture"
                    new_lecture = Session(session_type, course.name, course.students)
                    course_sessions.append(new_lecture)
                    session_list.append(new_lecture)

                # creates tutorials
                if course_specification[2] != "0":
                    num_students_tutorial = int(course_specification[3])
                    num_tutorials = int((float(num_students) / float(num_students_tutorial)) + 1)
                    rest = course.students
                    for i in range(num_tutorials):
                        students_tutorial = rest[:num_students_tutorial]

                        rest = rest[num_students_tutorial:]
                        session_type = "tutorial"
                        new_tutorial = Session(session_type, course.name, students_tutorial)
                        course_sessions.append(new_tutorial)
                        session_list.append(new_tutorial)

                # creates practica 
                if course_specification[4] != "0":
                    num_students_practicum = int(course_specification[5])
                    num_practicum = int((float(num_students) / float(num_students_practicum)) + 1)
                    rest = course.students
                    for i in range(num_practicum):
                        students_practicum = rest[:num_students_practicum]
                        rest = rest[num_students_practicum:]
                        session_type = "practicum"
                        new_practicum = Session(session_type, course.name, students_practicum)
                        course_sessions.append(new_practicum)
                        session_list.append(new_practicum)

    # extracts the specifications of every room
    room_specifications = [["A1.04",41], ["A1.06",22], ["A1.08",20,], ["A1.10",56], ["B0.201",48], ["C0.110",117], ["C1.112",60]]

    # print len(session_list)
    # for session in session_list:
    #     session.session_type
    #     print session.course
    #     print session.students

    # creates room objects
    room_list = []
    for room_specification in room_specifications:
        new_room = Room(room_specification[0], room_specification[1])
        print new_room.name
        print new_room.capacity
        room_list.append(new_room)

    # returns list of student objects and list of course objects
    return [student_list, course_list, session_list, room_list]
