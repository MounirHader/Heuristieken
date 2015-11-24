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



class TimeSlot(object):
    """
    A TimeSlot represents a two hour block.
    """
    def __init__(self, course, students):
        """
        Initializes a timeslot with day and hour

        """
        self.course = course
        self.students = students
        self.day = ''
        self.hour = ''

    def randomnDayHour(self):
        """
        Assigns randomn day and hour to timeslot

        """
        self.day = random.randint(0, 4)
        self.hour = random.randint(0,3)

    def isRoomEmpty(self, schedule_room):
        """
        returns true if timeslot is empty for room

        """
        for time_slot in schedule_room.time_slots:
            if self.day != time_slot.day or self.hour != time_slot.hour:
                return True

    def isStudentEmpty(self, schedule_student):
        """
        returns if timeslot is empty for student

        """

        for time_slot in schedule_student.time_slots:
            if self.day != time_slot.day or self.hour != time_slot.hour:
                return True



    def fillTimeSlot(self, schedule_room, schedule_student):
        """
        Fill timeslot to schedule_room and schedule_student

        """
        schedule_room.time_slots.append(self)
        schedule_student.time_slots.append(self)



class ScheduleRoom(object):
    """
    A ScheduleRoom represents a Schedule containing filled timeslots

    """
    def __init__(class_room):
        """
        Initializes a ScheduleRoom with a specified class_room

        Initially, no timeslots are filled with courses

        """

        self.class_room = class_room
        self.time_slots = []


class ScheduleStudent(object):
    """
    A ScheduleStudent represents a Schedule containing filled timeslots

    """

    def __init__(student):
        """
        Initializes a ScheduleStudent with a specified student

        Initially, no timeslots are filled with courses

        """

        self.class_room = student
        self.time_slots = []


def objectMaker():
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

    # creates one schedule_room object
    schedule_room = ScheduleRoom("A5")

    # creates 



# run last class
objectMaker()
