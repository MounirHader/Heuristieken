# leerlingen
leerling_1 = [wiskunde, natuurkunde]
leerling_2 = [natuurkunde]
leerling_3 = [scheikunde, natuurkunde]

# onderwijsvorm
vorm = [hoorcollege, werkcollege, practicum]

# list is vorm
vakken = {'wiskunde': [3, 2, 0], 'natuurkunde': [1, 2, 2], 'scheikunde': [1, 2, 4]}

# dingen
lokalen = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
tijdslot = [9, 11, 13, 15]
dagen = [...]


class Student
    """
    A Student represents a certain student

    """
    def __init__(self, identifier, courses):
        """
        Initializes a student with courses

        """
        self.identifier = identifier
        self.courses = courses

    def numberCourses(self):
        """
        returns number of courses

        """
        return len(self.courses)

class Course
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

class Class
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


class ScheduleStudent
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

def startinvullen rooster

voor iedere student maak een rooster animation

voor ieder ekamere
