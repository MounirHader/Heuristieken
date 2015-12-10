
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
    print "Random score"
    print score

    step = 0

    while(score < 1000):
        # only change score when new_score is higher
        tries = 0

        while (True):
            # select 2 random timeslots from random
            random_1 = random.choice(time_slot_list)
            random_2 = random.choice(time_slot_list)
            tries += 1

            # Switches two random timeslots in all relevant schedules
            switch(random_1, random_2, schedule_student_list, schedule_room_list)

            # calculates new score of incremental change
            new_score = score_function.main(schedule_room_list, schedule_student_list, course_list)

            # when new score is better take the step
            if new_score > score:
                score = new_score
                break
            # when the score is not better switch back
            else:
                switch(random_2, random_1, schedule_student_list, schedule_room_list)
                new_score = score_function.main(schedule_room_list, schedule_student_list, course_list)


        step += 1
        print "Step: " + str(step) + " , after: " + str(tries) + " tries"
        print score


    print "we are in the thousands"

def switch(random_1, random_2, schedule_student_list, schedule_room_list):
    """
    Switches two random timeslots in all relevant schedules
    """

    # select the room schedule were random 1 and 2 are held
    for schedule_room in schedule_room_list:
        if schedule_room.class_room == random_1.class_room:
            schedule_room_1 = schedule_room
        if schedule_room.class_room == random_2.class_room:
            schedule_room_2 = schedule_room

    # remove random_1 append random_2 in room schedule 1
    for time_slot in schedule_room_1.time_slots:
        if time_slot.day == random_1.day and time_slot.hour == random_1.hour:
            schedule_room_1.time_slots.remove(time_slot)
            schedule_room_1.time_slots.append(random_2)

    # remove random_2 append random_1 relevant student schedules
    for time_slot in schedule_room_2.time_slots:
        if time_slot.day == random_2.day and time_slot.hour == random_2.hour:
            schedule_room_2.time_slots.remove(time_slot)
            schedule_room_2.time_slots.append(random_1)

    # switches day hour and room of random 1 and 2
    day_bucket = random_1.day
    hour_bucket = random_1.hour
    room_bucket = random_1.class_room

    random_1.day = random_2.day
    random_1.hour = random_2.hour
    random_1.class_room = random_2.class_room

    random_2.day = day_bucket
    random_2.hour = hour_bucket
    random_2.class_room = room_bucket

# run the function
main()
