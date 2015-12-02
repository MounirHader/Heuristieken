import schedule_maker, sys, pygame

def visualize(schedule):
    pygame.init()

    background_color = (240,240,240)
    timeslot_color = (99,99,99)
    text_color = (0,0,0)
    display_x = 575
    display_y = 530

    gameDisplay = pygame.display.set_mode((display_x, display_y))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        # initialize window
        gameDisplay.fill(background_color)
        # screen = gameDisplay.fill(background_color, rect=[857,100,350,600])

        # put time_slot in visualization
        for time_slot in schedule.time_slots:
            pygame.draw.rect(gameDisplay, timeslot_color, [time_slot.day * 100 + 75, time_slot.hour * 100 + 30,100,100])

            # initialize font
            myfont = pygame.font.SysFont("helvetica", 18)
            myfont2 = pygame.font.SysFont("helvetica", 12)

            # render text
            label = myfont.render(time_slot.course[:7], 3, text_color)
            gameDisplay.blit(label, (time_slot.day * 100 + 75 + 15, time_slot.hour * 100 + 30 + 40))

            label2 = myfont2.render(time_slot.type, 3, text_color)
            gameDisplay.blit(label2, (time_slot.day * 100 + 75 + 20, time_slot.hour * 100 + 30 + 60))

        # headers font
        headerfont = pygame.font.SysFont("helvetica", 15)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        hours = ["09:00", "11:00", "13:00", "15:00", "17:00"]

        # draw header rectangles for days and hours
        pygame.draw.rect(gameDisplay, (189,189,189), [75, 0, 500, 30])
        pygame.draw.rect(gameDisplay, (189,189,189), [0, 30, 75, 500])

        # header text
        for i in range (5):
            # days header
            label = headerfont.render(days[i], 3, text_color)
            gameDisplay.blit(label, (92 + i* 100, 4))
            # hours header
            label2 = headerfont.render(hours[i], 3, text_color)
            gameDisplay.blit(label2, (32, 31 + i*100))

        # draw 5x5 grid
        for i in range(5):
            # horizontal lines
            pygame.draw.line(gameDisplay, (0,0,0), (0, i*100 + 30), (575, i*100 + 30))

            # vertical lines
            pygame.draw.line(gameDisplay, (0,0,0), (i * 100 + 75, 0), (i * 100 + 75, 575))

        # set correct caption
        if schedule.type == "room":
        	pygame.display.set_caption('Rooster: ' + schedule.class_room)
        else:
            pygame.display.set_caption('Rooster: ' + schedule.student_id)

        pygame.display.update()

# run main function in schedule_maker
schedule = schedule_maker.main()

schedule_room_list = schedule[0]
schedule_student_list = schedule[1]


for schedule_room in schedule_room_list:
    for time_slots in schedule_room.time_slots:
        print time_slots.day


# visualize room schedule
for schedule_room in schedule_room_list:
    visualize(schedule_room)

# visualize students schedules
for schedule_student in schedule_student_list[99:100]:
    visualize(schedule_student)
