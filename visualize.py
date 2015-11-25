import kleinprobleem, sys, pygame

# run scheduleMaker
schedule = kleinprobleem.scheduleMaker()

schedule_room = schedule[0]
schedule_student_list = schedule[1]



#
#
#
# print "Dit is zijn de timeslots voor het klaslokaal"
# for time_slot in schedule_room.time_slots:
#   print "course: "
#   print time_slot.name
#   print "students: "
#   print time_slot.students
#   print "day: "
#   print time_slot.day
#   print "hour: "
#   print time_slot.hour
#
# print "!!! Nu komen de timeslots  van de studenten !!!"
# for schedule_student in schedule_student_list:
#   print "Timeslots van: " + schedule_student.student_id
#   for time_slot in schedule_student.time_slots:
#       print "course: "
#       print time_slot.name
#       print "students: "
#       print time_slot.students
#       print "day: "
#       print time_slot.day
#       print "hour: "
#       print time_slot.hour

# monday
# if (time_slot.day == 0 && time_slot.hour == 0):


def visualize(schedule):
    pygame.init()

    black = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)
    gekkigheid = (255, 240, 240)
    grey = (158,158,158)

    display_x = 500
    display_y = 500

    gameDisplay = pygame.display.set_mode((display_x, display_y))
    pygame.display.set_caption('Gimmah')

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameDisplay.fill(gekkigheid)
        screen = gameDisplay.fill(grey, rect=[857,100,350,600])

        # put time_slot in visualization
        for time_slot in schedule.time_slots:
            pygame.draw.rect(gameDisplay, (202, 222, 218), [time_slot.day * 100 , time_slot.hour * 100 ,100,100])

            # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
            myfont = pygame.font.SysFont("comicsansms", 15)

            # render text
            label = myfont.render(time_slot.name[:3], 3, (0,0,0))
            gameDisplay.blit(label, (time_slot.day * 100 +30 , time_slot.hour * 100 + 40))

        # initialize 5x5 grid
        for i in range(5):
            # horizontal lines
            pygame.draw.line(gameDisplay, black, (0,i*100), (500, i*100))

            # vertical lines
            pygame.draw.line(gameDisplay, black, (i * 100,0), (i * 100 ,500))

        # put correct caption
        if schedule.type == "room":
        	pygame.display.set_caption('Rooster: ' + schedule.class_room)
        else:
            pygame.display.set_caption('Rooster: ' + schedule.student_id)

        pygame.display.update()

# visualize room schedule
visualize(schedule_room)

# visualize students schedules
for schedule_student in schedule_student_list:
    visualize(schedule_student)
