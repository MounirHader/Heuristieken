def main():
    import schedule_maker
    import preparation

    # creates a list of student and course objects in preparation file
    lists = preparation.main()
    student_list = lists[0]
    course_list = lists[1]
    session_list = lists[2]
    room_list = lists[3]

    schedule = schedule_maker.main(student_list, course_list, session_list, room_list)

    schedule_room_list = schedule[0]
    schedule_student_list = schedule[1]
    course_list = schedule[2]


    score = 1000

    # bonus and malus of course activities over week for student
    for schedule_student in schedule_student_list:
        # print schedule_student.student_id

        # loops over every possible course
        for course in course_list:

            # adds timeslots of specific course to list
            time_slot_student_course = []
            for time_slot in schedule_student.time_slots:
                if time_slot.course == course.name:
                    # print course.name
                    time_slot_student_course.append(time_slot)

            # list of how activities are spread of specific course for student
            spread_activities = []

            # spread of mo-th and tu-fr when two activities
            if len(time_slot_student_course) == 2:
                for time_slot in time_slot_student_course:
                    spread_activities.append(time_slot.day)
                    if spread_activities == [0, 3] or spread_activities == [1, 4] or spread_activities == [3, 0] or spread_activities == [4, 1]:
                        score += 1
                # print "spread_activities:"
                # print spread_activities

            # spread of mo-we-fr when three activities
            elif len(time_slot_student_course) == 3:
                for time_slot in time_slot_student_course:
                    spread_activities.append(time_slot.day)
                    if spread_activities == [0, 2, 4] or spread_activities == [0, 4, 2] or spread_activities == [2, 0, 4] or spread_activities == [4, 0, 2] or spread_activities == [4, 2, 0] or spread_activities == [2, 4, 0]:
                        score += 1
                # print "spread_activities:"
                # print spread_activities

            # spread of mo-tu-th-fr when four activities
            elif len(time_slot_student_course) == 4:
                for time_slot in time_slot_student_course:
                    spread_activities.append(time_slot.day)
                    if spread_activities == [0, 1, 3, 4] or spread_activities == [0, 3, 1, 4] or spread_activities == [0, 1, 4, 3] or spread_activities == [0, 3, 4, 1] or spread_activities == [0, 4, 3, 1] or spread_activities == [0, 4, 1, 3] or spread_activities == [1, 0, 3, 4] or spread_activities == [1, 0, 4, 3] or spread_activities == [1, 3, 0, 4] or spread_activities == [1, 3, 4, 0] or spread_activities == [1, 4, 3, 0] or spread_activities == [1, 4, 0, 3] or spread_activities == [3, 0, 1, 4] or spread_activities == [3, 0, 4, 1] or spread_activities == [3, 1, 4, 0] or spread_activities == [3, 1, 0, 4] or spread_activities == [3, 4, 0, 1] or spread_activities == [3, 4, 1, 0] or spread_activities == [4, 0, 1, 3] or spread_activities == [4, 0, 3, 1] or spread_activities == [4, 1, 3, 0] or spread_activities == [4, 1, 0, 3] or spread_activities == [4, 3, 0, 1] or spread_activities == [4, 3, 1, 0]:
                        score += 1
                # print "spread_activities:"
                # print spread_activities

            # count number of days with an activity for a student
            days_of_activities = []
            spread_days = 0

            # for loop to extract the days with an activity on it and append in list days_of_activities
            for i in range (len(spread_activities)):
                if spread_activities[i] not in days_of_activities:
                    days_of_activities.append(spread_activities[i])

            spread_days = len(days_of_activities)

            # substract more score when there is less spread of activities
            if spread_days == (len(spread_activities) - 1):
                score -= 0.5
                # print "- 0.5"
            elif spread_days == len(spread_activities) - 2:
                score -= 1
                # print "- 1"
            elif spread_days == len(spread_activities) - 3:
                score -= 1.5
                # print "- 1.5"

        # subtract points for student schedule conflicts
        timeslot_list = schedule_student.giveList()
        for timeslot in timeslot_list:
            if (timeslot_list.count(timeslot) != 1):
                conflict_aftrek = timeslot_list.count(timeslot) - 1
                score -= conflict_aftrek

    # subtract points for overcapacity in room
    for schedule_room in schedule_room_list:
        capacity = schedule_room.capacity
        for time_slot in schedule_room.time_slots:
            if len(time_slot.students) > capacity:
                malus_room = len(time_slot.students) - capacity
                score -= malus_room

    return score
