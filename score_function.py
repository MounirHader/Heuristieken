import kleinprobleem

schedule = kleinprobleem.scheduleMaker()

schedule_room = schedule[0]
schedule_student_list = schedule[1]


# # print "Dit is zijn de timeslots voor het klaslokaal"
# for time_slot in schedule_room.time_slots:
#     print "course: "
#     print time_slot.name
#     print "students: "
#     print time_slot.students
#     print "day: "
#     print time_slot.day
#     print "hour: "
#     print time_slot.hour
#
print "!!! Nu komen de timeslots  van de studenten !!!"
for schedule_student in schedule_student_list:
    print "Timeslots van: " + schedule_student.student_id
    for time_slot in schedule_student.time_slots:
        print "course: "
        print time_slot.name
        print "students: "
        print time_slot.students
        print "day: "
        print time_slot.day
        print "hour: "
        print time_slot.hour

score = 1000

# bonus when spread of activities over week
for schedule_student in schedule_student_list:
    print "new student"
    # a list whit the spread of the activities over the week e.g. mo-th is [0, 3]
    spread_days = []
    # spread of mo-th and tu-fr when two activities
    if len(schedule_student.time_slots) == 2:
        for time_slot in schedule_student.time_slots:
            spread_days.append(time_slot.day)
            print "spread_days:"
            print spread_days
            if spread_days == [0, 3] or spread_days == [1, 4] or spread_days == [3, 0] or spread_days == [4, 1]:
                score += 20

    # spread of mo-we-fr when three activities
    if len(schedule_student.time_slots) == 3:
        for time_slot in schedule_student.time_slots:
            spread_days.append(time_slot.day)
            print "spread_days:"
            print spread_days
            if spread_days == [0, 2, 4] or spread_days == [0, 4, 2] or spread_days == [2, 0, 4] or spread_days == [4, 0, 2] or spread_days == [4, 2, 0] or spread_days == [2, 4, 0]:
                score += 30

    # spread of mo-tu-th-fr when four activities
    if len(schedule_student.time_slots) == 4:
        for time_slot in schedule_student.time_slots:
            spread_days.append(time_slot.day)
            print "spread_days:"
            print spread_days
            if spread_days == [0, 1, 3, 4] or spread_days == [0, 3, 1, 4] or spread_days == [0, 1, 4, 3] or spread_days == [0, 3, 4, 1] or spread_days == [0, 4, 3, 1] or spread_days == [0, 4, 1, 3] or spread_days == [1, 0, 3, 4] or spread_days == [1, 0, 4, 3] or spread_days == [1, 3, 0, 4] or spread_days == [1, 3, 4, 0] or spread_days == [1, 4, 3, 0] or spread_days == [1, 4, 0, 3] or spread_days == [3, 0, 1, 4] or spread_days == [3, 0, 4, 1] or spread_days == [3, 1, 4, 0] or spread_days == [3, 1, 0, 4] or spread_days == [3, 4, 0, 1] or spread_days == [3, 4, 1, 0] or spread_days == [4, 0, 1, 3] or spread_days == [4, 0, 3, 1] or spread_days == [4, 1, 3, 0] or spread_days == [4, 1, 0, 3] or spread_days == [4, 3, 0, 1] or spread_days == [4, 3, 1, 0]:
                score += 40

    # count number of days with an activity for a student
    days_of_activities = []
    number_of_days = 0
    # for loop to extract the days with an activity on it and append in list days_of_activities
    for i in range (len(spread_days)):
        if spread_days[i] not in days_of_activities:
            days_of_activities.append(spread_days[i])
    print "list:"
    print days_of_activities
    # the length of days_of_activities is the amount of days with an activity for a student
    number_of_days = len(days_of_activities)
    print "number of days:"
    print number_of_days

    # substract more score when there is less spread of activities
    if number_of_days == (len(spread_days) - 1):
        score -= 10
    if number_of_days == len(spread_days) - 2:
        score -= 20
    if number_of_days == len(spread_days) - 3:
        score -= 30
print score
#     # overschreiding van zaalcapaciteit
#     if studenten_ingedeeld_in_zaal > zaalcapaciteit:
#         overeschreiding = studenten_ingedeeld_in_zaal - zaalcapaciteit:
#         score = score - overeschreiding
#
#     # roosterconflict student
#     if student heeft twee keer zelfde tijdslot:
#         score = score - 1
