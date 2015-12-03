
def main():

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

    score = score_function.main(schedule_room_list, schedule_student_list, course_list)
    print "random score"
    print score

    step = 0

    while(score < 1000):
        # only change score when new_score is higher
        tries = 0
        new_score = -1000

        while (True):
            # select 2 random timeslots from random
            random_1 = random.choice(time_slot_list)
            random_2 = random.choice(time_slot_list)
            tries += 1

            # Switches two random timeslots in all relevant schedules
            switch(random_1, random_2, schedule_student_list, schedule_room_list)

            # calculates new score of incremental change
            new_score = score_function.main(schedule_room_list, schedule_student_list, course_list)
            print new_score

            # when new score is better take the step
            if new_score > score:
                score = new_score
                break
            # when the score is not better switch back
            else:
                switch(random_1, random_2, schedule_student_list, schedule_room_list)
                print "switch back"
                new_score = score_function.main(schedule_room_list, schedule_student_list, course_list)
                print new_score


        step += 1
        score = new_score
        print "step: " + str(step) + "tries:" + str(tries)
        print score


    print "we are positive"

def switch(random_1, random_2, schedule_student_list, schedule_room_list):
    """
    Switches two random timeslots in all relevant schedules
    """

    # append all the schedules from students that follow random 1 and 2 in lists
    schedule_students_1 = []
    schedule_students_2 = []
    for schedule_student in schedule_student_list:
        for student in random_1.students:
            if student == schedule_student.student_id:
                schedule_students_1.append(schedule_student)
        for student in random_2.students:
            if student == schedule_student.student_id:
                schedule_students_2.append(schedule_student)

    # remove random_1 append random_2 from relevant student schedules
    for schedule_student in schedule_students_1:
        for time_slot in schedule_student.time_slots:
            if time_slot.type == random_1.type and time_slot.course == random_1.course:
                schedule_student.time_slots.remove(time_slot)
                schedule_student.time_slots.append(random_2)
                time_slot.class_room = random_2.class_room

    # remove random_2 append random_1 relevant student schedules
    for schedule_student in schedule_students_2:
        for time_slot in schedule_student.time_slots:
            if time_slot.type == random_2.type and time_slot.course == random_1.course:
                schedule_student.time_slots.remove(time_slot)
                schedule_student.time_slots.append(random_1)
                time_slot.class_room = random_1.class_room

    # select the room schedule were random 1 and 2 are held
    for schedule_room in schedule_room_list:
        if schedule_room.class_room == random_1.class_room:
            schedule_room_1 = schedule_room
        if schedule_room.class_room == random_2.class_room:
            schedule_room_2 = schedule_room


    # remove random_1 append random_2 in room schedule 1
    for time_slot in schedule_room_1.time_slots:
        if time_slot.type == random_1.type and time_slot.course == random_1.course:
            schedule_room_1.time_slots.remove(time_slot)
            schedule_room_1.time_slots.append(random_2)
            time_slot.class_room = random_2.class_room

    # remove random_2 append random_1 relevant student schedules
    for time_slot in schedule_room_2.time_slots:
        if time_slot.type == random_2.type and time_slot.course == random_1.course:
            schedule_room_2.time_slots.remove(time_slot)
            schedule_room_2.time_slots.append(random_1)
            time_slot.class_room = random_1.class_room

# run the function
main()
