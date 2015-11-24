import kleinprobleem

# run scheduleMaker
schedule = kleinprobleem.scheduleMaker()

schedule_room = schedule[0]
schedule_student_list = schedule[1]

print "Dit is zijn de timeslots voor het klaslokaal"
for time_slot in schedule_room.time_slots:
  print "course: "
  print time_slot.name
  print "students: "
  print time_slot.students
  print "day: "
  print time_slot.day
  print "hour: "
  print time_slot.hour

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
