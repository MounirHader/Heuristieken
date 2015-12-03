import preparation
import schedule_maker
import random
import score_function

# creates a list of student and course objects in preparation file
lists = preparation.main()
student_list = lists[0]
course_list = lists[1]
session_list = lists[2]
room_list = lists[3]

#  creates schedule with schedules for room and students
schedule = schedule_maker.main(student_list, course_list, session_list, room_list)
schedule_room_list = schedule[0]
schedule_student_list = schedule[1]
course_list = schedule[2]
time_slot_list = schedule[3]

score_1 = score_function.main(schedule_room_list, schedule_student_list, course_list)
print "score 1"
print score_1

# select 2 random timeslots from random
random_1 = random.choice(time_slot_list)
random_2 = random.choice(time_slot_list)


# switch die 2 timeslots in de roosters die relevant zijn
for schedule_student in random_1.schedule_students:
    # remove and append time_slot in schedules van students
    for time_slot in schedule_student.time_slots:
        if time_slot.type == random_1.type and time_slot.course == random_1.course:
            schedule_student.time_slots.remove(time_slot)
            schedule_student.time_slots.append(random_2)

# remove and append time_slot in schedule van room
for time_slot in random_1.schedule_room[0].time_slots:
    if time_slot.type == random_1.type and time_slot.course == random_1.course:
        random_1.schedule_room[0].time_slots.remove(time_slot)
        random_1.schedule_room[0].time_slots.append(random_2)

# switch die 2 timeslots in de roosters die relevant zijn
for schedule_student in random_2.schedule_students:
    # remove and append time_slot in schedules van students
    for time_slot in schedule_student.time_slots:
        if time_slot.type == random_2.type and time_slot.course == random_1.course:
            schedule_student.time_slots.remove(time_slot)
            schedule_student.time_slots.append(random_1)

# remove and append time_slot in schedule van room
for time_slot in random_2.schedule_room[0].time_slots:
    if time_slot.type == random_2.type and time_slot.course == random_1.course:
        random_2.schedule_room[0].time_slots.remove(time_slot)
        random_2.schedule_room[0].time_slots.append(random_1)

score_2 = score_function.main(schedule_room_list, schedule_student_list, course_list)
print "score 2"
print score_2
