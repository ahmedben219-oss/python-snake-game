import pygame #loads the pygame libary so we can use its tools like drawing
pygame.init() # sets up pygame internal system ( graphics, sounds etc) must always run first
import Snake

screen = pygame.display.set_mode((600,400))
cell_size = 20 # since our window is 600 x 400 this gives me 30 columns x 20 rows
#creates the actual game window and its dimensions and can be recalled when we use the variable screen
pygame.display.set_caption("Snake")
# all this does is make the text "Snake" as the title in the game window 

clock = pygame.time.Clock()
while Snake.running: #just a loop that keeps repeating as long as the game is running, main game loop
    for event in pygame.event.get(): #pygame.event.get is asking python what has happened since i last checked
        #this loops for every event checking to see what happened
        if event.type == pygame.QUIT: 
            # if while wer're checking every event we come across pygame.QUIT we end the while loop
            Snake.running = False #flipping the switch off from true, ending the loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                  Snake.direction = "UP"
            elif event.key == pygame.K_DOWN:
                  Snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                  Snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                  Snake.direction = "RIGHT"
    Snake.move_snake()
    screen.fill((0,0,0))# paints the entire window one solid color following the RGB scheme
    for x in range(0, 600, cell_size):
            pygame.draw.line(screen, (40,40,40), (x,0), (x,400))
    for y in range(0, 400, cell_size):
            pygame.draw.line(screen, (40,40,40), (0,y), (600,y))
    for col in range(0,30):
          for row in range(0,20):
                if (col + row) % 2 == 0:
                      colour = (102,255,102)
                else:
                      colour = (0,153,0)
                pygame.draw.rect(screen, colour, (col * cell_size, row * cell_size, cell_size, cell_size)) 
    Snake.draw_snake(screen)
    pygame.display.update() #pygame won't show our drawing until we tell it to refresh.
    print(Snake.direction)
    clock.tick(10)
Snake.game_over_screen(screen, Snake.score) 
pygame.quit # quits the game 
