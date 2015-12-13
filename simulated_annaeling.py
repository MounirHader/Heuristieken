import preparation
import schedule_maker
import random
import score_function
# import visualize
import csv
import math

def main():
    # creates a list of student and course objects in preparation file
    lists = preparation.main()
    student_list = lists[0]
    course_list = lists[1]
    session_list = lists[2]
    room_list = lists[3]

    # executes simulated annealing
    schedule = simulated_annealing(student_list, course_list, session_list, room_list)
    schedule_room_list = schedule[0]
    schedule_student_list = schedule[1]
    data = schedule[2]

    # writes data of schedule  to csv
    with open('data_simulated_annealing.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['Step', 'Score', 'Tries'])
        for row in data:
            writer.writerow(row)

    # # visualizes room schedules
    # schedule_room_list = max_schedule[0]
    # schedule_student_list = max_schedule[1]
    # for schedule_room in schedule_room_list:
    #     visualize.visualize(schedule_room)
    #
    # # visualize students schedules
    # for schedule_student in schedule_student_list[151:152]:
    #     visualize.visualize(schedule_student)
    #
    # for schedule_student in schedule_student_list[155:156]:
    #     visualize.visualize(schedule_student)


def simulated_annealing(student_list, course_list, session_list, room_list):

    """
    Starts at random schedule and climbs the hill.
    Probability of acceptance reduces when temperature cools down
    """

    #  creates schedule with schedules for room and students
    schedule = schedule_maker.main(student_list, course_list, session_list, room_list)
    schedule_room_list = schedule[0]
    schedule_student_list = schedule[1]
    course_list = schedule[2]
    time_slot_list = schedule[3]
    score = score_function.main(schedule_room_list, schedule_student_list, course_list)
    step = 0

    # initiates temperature (certain acceptance prob of 0.8)
    temperature = 10

    # initiates cooling_rate
    cooling_rate = 0.001

    # were tries and scores per step are saved
    data = []

    while(True):
        # only change score when new_score is higher
        tries = 0

        while (True):
            # select 2 random timeslots from random
            random_1 = random.choice(time_slot_list)
            random_2 = random.choice(time_slot_list)
            tries += 1

            # cools the temperature
            temperature *= 1 - cooling_rate

            # Switches two random timeslots in all relevant schedules
            switch(random_1, random_2, schedule_student_list, schedule_room_list)

            # calculates new score of incremental change
            new_score = score_function.main(schedule_room_list, schedule_student_list, course_list)

            # calculates probability of acceptance
            prob = acceptance_probability(score, new_score, temperature)

            # when probability of acceptance is higher then random number between 0 and 1 take a step
            if prob > random.random():
                score = new_score
                break
            # when the score is not better switch back
            else:
                switch(random_2, random_1, schedule_student_list, schedule_room_list)
                new_score = score_function.main(schedule_room_list, schedule_student_list, course_list)

            # ends function if temperature is below 1
            if temperature < 1:
                return [schedule_room_list, schedule_student_list, data]


        step += 1

        print "Step: " + str(step) + " Score: " + str(score) + " Tries: " + str(tries) + " Temp: " + str(temperature)

        # saves the data for this step in data list
        data_step = []
        data_step.append(step)
        data_step.append(score)
        data_step.append(tries)
        data.append(data_step)

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


def acceptance_probability(score, new_score, temperature):
    """
    Calculates the probability of acceptance of a trie
    """
    # when new score is better acceptance is sure
    if (new_score > score):
        return 1.0

    # if the new sore is worse calculate acceptance probability
    return math.exp((new_score - score) / temperature)

main()
