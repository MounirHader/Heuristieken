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
    spread_days = []
    # spread of mo-th and tu-fr when two activities
    if len(schedule_student.time_slots) == 2:
        for time_slot in schedule_student.time_slots:
            spread_days.append(time_slot.day)
            print spread_days
        if spread_days[0] == 0 and spread_days[1] == 3 or spread_days[0] == 1 and spread_days[1] == 4:
            score += 20

    # spread of mo-we-fr when three activities
    if len(schedule_student.time_slots) == 3:
        for time_slot in schedule_student.time_slots:
            spread_days.append(time_slot.day)
            print spread_days
        if spread_days[0] == 0 and spread_days[1] == 2 and spread_days[2] == 4:
            score += 30

    # spread of mo-tu-th-fr when four activities
    if len(schedule_student.time_slots) == 4:
        for time_slot in schedule_student.time_slots:
            spread_days.append(time_slot.day)
            print spread_days
        if spread_days[0] == 0 and spread_days[1] == 1 and spread_days[2] == 3 and spread_days[3] == 4:
            score += 40

print score


#     # maluspunten voor slechte spreiding
#     if dagen met activiteiten = activiteiten van student - 1:
#         score = score - 10
#     if dagen met activiteiten = activiteiten van student - 2:
#         score = score - 20
#     if dagen met activiteiten = activiteiten van student - 3:
#         score = score - 30
#
#     # overschreiding van zaalcapaciteit
#     if studenten_ingedeeld_in_zaal > zaalcapaciteit:
#         overeschreiding = studenten_ingedeeld_in_zaal - zaalcapaciteit:
#         score = score - overeschreiding
#
#     # roosterconflict student
#     if student heeft twee keer zelfde tijdslot:
#         score = score - 1
