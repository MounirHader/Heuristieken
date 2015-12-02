import preparation
import score_function
import schedule_maker


# creates a list of student and course objects in preparation file
lists = preparation.main()
student_list = lists[0]
course_list = lists[1]
session_list = lists[2]
room_list = lists[3]

# for i in range(100):
#     schedule = schedule_maker.main(student_list, course_list, session_list, room_list)
#     print i

for i in range (100):
    score = score_function.main()
    print score
