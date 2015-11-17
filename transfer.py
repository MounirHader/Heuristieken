import csv

# open csv file and reads into csv-file
f = open('studenten_roostering.csv')
csv_file = csv.reader(f)

courses_info = []
empty_list = []
course_len = ''

# extracts the id and courses of every student
for student_info in csv_file:
    student_id = student_info[2]
    courses_student = student_info[3:]

    # loops over courses of the student
    for course_student in courses_student:
        course_exists = False
        # checks if course already exist in courses_info
        for course_info in courses_info:
            if course_info[0] == course_student:
                course_info.append(student_id)
                course_exists = True
        if course_exists == False:
            if course_student != '':
                course_list = [course_student, course_len]
                courses_info.append(course_list)

# determines the course lenght of the course
for course_info in courses_info:
    course_info[1] = len(course_info) - 1

courses_info = courses_info[5:]
print courses_info

output = open('vakken_roostering.csv', 'wb')
writer = csv.writer(output)
for course_info in courses_info:
    writer.writerow(course_info)
