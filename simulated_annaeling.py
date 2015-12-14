import preparation
import schedule_maker
import random
import score_function
import visualize
import csv
import math

def main():
    # creates a list of student and course objects in preparation file
    lists = preparation.main()
    student_list = lists[0]
    course_list = lists[1]
    session_list = lists[2]
    room_list = lists[3]

    score_max = 0

    # searches 5 times for a local maximum and visualizes the best score
    for i in range(5):
        print i
        # executes simulated annealing
        local_max_schedule = simulated_annealing(student_list, course_list, session_list, room_list)
        schedule_room_list = local_max_schedule[0]
        schedule_student_list = local_max_schedule[1]
        score_list = score_function.main(schedule_room_list, schedule_student_list, course_list)
        score_local_max = score_list[0]

        # when new hillclimber score is better
        if score_local_max > score_max:
            max_schedule = local_max_schedule
            score_max = score_local_max

    data = max_schedule[2]
    # writes data of schedule  to csv
    with open('data_simulated_annealing.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['Iteration', 'Score', 'malus_conflict', 'malus_capacity', 'malus_spread', 'bonus_spread'])
        for row in data:
            writer.writerow(row)

    # visualizes room schedules
    schedule_room_list = max_schedule[0]
    schedule_student_list = max_schedule[1]
    for schedule_room in schedule_room_list:
        visualize.visualize(schedule_room)

    # visualize students schedules
    for schedule_student in schedule_student_list[151:152]:
        visualize.visualize(schedule_student)

    for schedule_student in schedule_student_list[155:156]:
        visualize.visualize(schedule_student)


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
    new_score_list = score_function.main(schedule_room_list, schedule_student_list, course_list)
    score = new_score_list[0]
    malus_conflict = new_score_list[1]
    malus_capacity = new_score_list[2]
    malus_spread = new_score_list[3]
    bonus_spread = new_score_list[4]

    # sets simulated annaeling to True
    sim = True

    # initiates temperature (certain acceptance prob of 0.8)
    temperature = 1000

    # initiates cooling_rate
    cooling_rate = 0.0001

    # were tries and scores per step are saved
    data = []
    iteration = 0

    while(True):
        # only change score when new_score is higher
        tries = 0

        while (True):

            # saves the data for this iteration in data list
            data_iteration = []
            data_iteration.append(iteration)
            data_iteration.append(score)
            data.append(data_iteration)
            data_iteration.append(malus_conflict)
            data_iteration.append(malus_capacity)
            data_iteration.append(malus_spread)
            data_iteration.append(bonus_spread)
            data.append(data_iteration)

            # select 2 random timeslots from random
            random_1 = random.choice(time_slot_list)
            random_2 = random.choice(time_slot_list)
            tries += 1
            iteration += 1

            # Switches two random timeslots in all relevant schedules
            switch(random_1, random_2, schedule_student_list, schedule_room_list)

            # calculates new score of incremental change
            new_score_list = score_function.main(schedule_room_list, schedule_student_list, course_list)
            new_score = new_score_list[0]

            # calculates probability of acceptance
            prob = acceptance_probability(score, new_score, temperature)

            # if simulated annaeling is on
            if sim:
                # cools the temperature
                temperature *= 1 - cooling_rate
                # when probability of acceptance is higher then random number between 0 and 1 take a step
                if prob > random.random():
                    score = new_score
                    malus_conflict = new_score_list[1]
                    malus_capacity = new_score_list[2]
                    malus_spread = new_score_list[3]
                    bonus_spread = new_score_list[4]
                    break
                # when the score is not better switch back
                else:
                    switch(random_2, random_1, schedule_student_list, schedule_room_list)

            # when simulated annaeling is over start hillclimber
            else:
                # when new score is better take the step
                if new_score > score:
                    score = new_score
                    break
                # when the score is not better switch back
                else:
                    switch(random_2, random_1, schedule_student_list, schedule_room_list)
                    new_score = score_function.main(schedule_room_list, schedule_student_list, course_list)

                # ends function if he tries more then 5000 steps
                if tries > 10000:
                    return [schedule_room_list, schedule_student_list, data]

            # ends function if temperature is below 1
            if temperature < 1:
                sim = False

        # print "Iteration: " + str(iteration) + " Score: " + str(score) + " Tries: " + str(tries) + " Temp: " + str(temperature)



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
