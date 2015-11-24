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
    def __init__(self, course):
        """
        Initializes a timeslot with day and hour

        """
        self.name = course.name
        self.students = course.students
        self.day = ''
        self.hour = ''

    def randomDayHour(self):
        """
        Assigns randomn day and hour to timeslot

        """
        import random
        self.day = random.randint(0,4)
        self.hour = random.randint(0,3)

    def isRoomEmpty(self, schedule_room):
        """
        returns true if timeslot is empty for room

        """
        room_empty = True

        if schedule_room.time_slots != []:
            for time_slot in schedule_room.time_slots:
                if self.day == time_slot.day and self.hour == time_slot.hour:
                    room_empty = False
        return room_empty


    def isStudentEmpty(self, schedule_student):
        """
        returns true if timeslot is empty for student

        """
        student_empty = True

        if schedule_student.time_slots != []:
            for time_slot in schedule_student.time_slots:
                if self.day == time_slot.day and self.hour == time_slot.hour:
                    student_empty = False
        return student_empty


    def fillTimeSlot(self, schedule_room, schedule_students_timeslot):
        """
        Fill timeslot to schedule_room and schedule_students_timeslot

        """
        schedule_room.time_slots.append(self)

        for schedule_student in schedule_students_timeslot:
            schedule_student.time_slots.append(self)



class ScheduleRoom(object):
    """
    A ScheduleRoom represents a Schedule containing filled timeslots

    """
    def __init__(self, class_room):
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

    def __init__(self, student_id):
        """
        Initializes a ScheduleStudent with a specified student

        Initially, no timeslots are filled with courses

        """

        self.student_id = student_id
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
    schedule_room = ScheduleRoom('A5')

    # creates the schedule_student objects
    schedule_student_list = []
    for student in student_list:
        schedule_student = ScheduleStudent(student.student_id)
        schedule_student_list.append(schedule_student)

    # creates timeslot object for every course
    time_slot_list = []

    print_list = []

    for course in course_list:
        time_slot = TimeSlot(course)

        # make list of schedule_student objects one for every student in this time_slot
        schedule_students_timeslot = []
        for student in time_slot.students:
            for schedule_student in schedule_student_list:
                if student == schedule_student.student_id:
                     schedule_students_timeslot.append(schedule_student)


        # assign random hour and day to time_slot
        time_slot.randomDayHour()

        while(True):

            # check if room is filled at timeslot
            room_empty = time_slot.isRoomEmpty(schedule_room)

            # checks if student are filled at timeslot
            for schedule_student in schedule_students_timeslot:
                student_empty = time_slot.isStudentEmpty(schedule_student)

                # if student_empty is false break out of for loop
                if student_empty == False:
                    break

            # checks if room_empty and student_empty are both true
            if room_empty == True and student_empty == True:
                #  fill schedule_room and schedule_stude
                time_slot.fillTimeSlot(schedule_room, schedule_students_timeslot)
                # break out of while loop
                break
            # else assign random day and hour to time_slot and check again
            else:
                time_slot.randomDayHour()

        # appends time_slot to time_slot_list
        time_slot_list.append(time_slot)

        # test
        test = [time_slot.name[:2],time_slot.day, time_slot.hour]
        print_list.append(test)
        print print_list




# run last class
objectMaker()
