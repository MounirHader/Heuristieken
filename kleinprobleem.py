

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

class Class(object):
    """
    A Class represents a a certain class of a course.
    """
    def __init__(self, course, class_type, students):
        """
        Initializes a class with class_type and students

        """
        self.course = course
        self.class_type = class_type
        self.students = students

    def numberStudents(self):
        """
        returns number of students

        """
        return len(self.students)


class TimeSlot(object):
    """
    A TimeSlot represents a two hour block.
    """
    def __init__(self, day, hour):
        """
        Initializes a timeslot with day and hour

        """
        self.day = day
        self.hour = hour


class ScheduleRoom(object):
    """
    A ScheduleRoom represents a Schedule containing filled or empty timeslots

    """
    def __init__(class_room):
        """
        Initializes a ScheduleRoom with a specified class_room

        A schedule has always days of 4 and hours of 3

        Initially, no timeslots are filled with courses

        """

        self.class_room = class_room
        self.days = 4
        self.hours = 3
        self.time_slots = []

    def fillTimeSlot(self, time_slot, course):
        """
        Fill time_slot with course

        """
        x = time_slot.day
        y = time_slot.hour
        if (x, y) not in self.time_slots:
            self.time_slots.append((x,y))

    def isTimeSlotFilled(self, m, n):
        """
        Return True if the time_slot (m, n) has been filled.

        Assumes that (m, n) represents a valid timeslot inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m, n) in self.time_slots


class ScheduleStudent(object):
    """
    A ScheduleStudent represents a Schedule containing filled or empty timeslots

    """

    def __init__(student):
        """
        Initializes a ScheduleStudent with a specified student

        A schedule has always days of 4 and hours of 3

        Initially, no timeslots are filled with courses

        """

        self.class_room = student
        self.days = 4
        self.hours = 3
        self.time_slots = []


    def fillTimeSlot(self, time_slot, course):
        """
        Fill time_slot with course

        """
        x = time_slot.day
        y = time_slot.hour
        if (x, y) not in self.time_slots:
            self.time_slots.append((x,y))

    def isTimeSlotFilled(self, m, n):
        """
        Return True if the time_slot (m, n) has been filled.

        Assumes that (m, n) represents a valid timeslot inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m, n) in self.time_slots

def makeSchedules():

    import csv

    # open csv file and reads into csv-file
    f = open('studenten_roostering.csv')
    csv_file = csv.reader(f)

    # empty list for student and course objects
    student_list = []
    course_list = []

    # extracts the id and courses of every student
    for student_info in csv_file:
        student_id = student_info[2]
        courses_student = student_info[3:]

        # create new student object and adds it to list
        student = Student(student_id, courses_student)
        print student.numberCourses()

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
