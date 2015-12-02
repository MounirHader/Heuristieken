

class TimeSlot(object):
    """
    A TimeSlot represents a two hour block.
    """
    def __init__(self, session):
        """
        Initializes a timeslot with day and hour

        """
        self.type = session.session_type
        self.course = session.course
        self.students = session.students
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
    def __init__(self, room):
        """
        Initializes a ScheduleRoom with a specified class_room

        Initially, no timeslots are filled with courses

        """

        self.class_room = room.name
        self.time_slots = []
        self.type = "room"
        self.capacity = room.capacity

    def giveList(self):
        """
        returns list of day and hours for schedule

        """
        schedule_list = []
        for time_slot in self.time_slots:
            day_hour = []
            day_hour.append(time_slot.day)
            day_hour.append(time_slot.hour)
            schedule_list.append(day_hour)

        return schedule_list




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
        self.type = "student"

    def giveList(self):
        """
        returns list of day and hours for schedule

        """
        schedule_list = []
        for time_slot in self.time_slots:
            day_hour = []
            day_hour.append(time_slot.day)
            day_hour.append(time_slot.hour)
            schedule_list.append(day_hour)

        return schedule_list

def main(student_list, course_list, session_list, room_list):
    '''
    Creates a schedule for room and students.

    Outputs: schedule_room object and schedule_student_list which is a list of objects
    '''

    # creates one schedule_room object
    schedule_room_list = []
    for room in room_list:
        schedule_room = ScheduleRoom(room)
        schedule_room_list.append(schedule_room)

    # creates the schedule_student objects
    schedule_student_list = []
    for student in student_list:
        schedule_student = ScheduleStudent(student.student_id)
        schedule_student_list.append(schedule_student)

    # creates timeslot object for every session
    time_slot_list = []
    print_list = []


    for session in session_list:
        time_slot = TimeSlot(session)

        # make list of schedule_student objects one for every student in this time_slot
        schedule_students_timeslot = []
        for student in time_slot.students:
            for schedule_student in schedule_student_list:
                if student == schedule_student.student_id:
                     schedule_students_timeslot.append(schedule_student)


        # assign random hour and day to time_slot
        time_slot.randomDayHour()

        import random
        schedule_room = random.choice(schedule_room_list)


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
            # if room_empty == True and student_empty == True:
            if room_empty == True:
                #  fill schedule_room and schedule_stude
                time_slot.fillTimeSlot(schedule_room, schedule_students_timeslot)
                # break out of while loop
                break
            # else assign random day and hour to time_slot and check again
            else:
                time_slot.randomDayHour()
                schedule_room = random.choice(schedule_room_list)


        # appends time_slot to time_slot_list
        time_slot_list.append(time_slot)

        # test
        test = [time_slot.course[:2],time_slot.day, time_slot.hour]
        print_list.append(test)
        # print print_list

    # print schedule_room.giveList()

    return [schedule_room_list, schedule_student_list, course_list]
