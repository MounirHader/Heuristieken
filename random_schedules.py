import preparation
import score_function
import schedule_maker


# creates a list of student and course objects in preparation file
lists = preparation.main()
student_list = lists[0]
course_list = lists[1]
session_list = lists[2]
room_list = lists[3]

number_courses = len(course_list)
total_students = 0
for course in course_list:
    number_students = len(course.students)
    total_students += number_students

avg_students = total_students / number_courses
print avg_students


# # create 100 schedules
# for i in range (100):
#     # create schedule
#     schedule = schedule_maker.main(student_list, course_list, session_list, room_list)
#
#     schedule_room_list = schedule[0]
#     schedule_student_list = schedule[1]
#     course_list = schedule[2]
#
#     # create score for schedule
#     score = score_function.main(schedule_room_list, schedule_student_list, course_list)
#     print score
