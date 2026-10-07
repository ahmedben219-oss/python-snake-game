import pygame
pygame.init()
font = pygame.font.SysFont(None, 36)
import random

pygame.mixer.init()
eat_sound = pygame.mixer.Sound("apple.mp3")
gameOverSound = pygame.mixer.Sound("gameOver.mp3")

running = True
cell_size = 20
snake = [(10,10), (9,10), (8,10)]
direction = "RIGHT"
food = (15, 10)
score = 0

def draw_snake(screen):
    for segment in snake:
        x, y = segment
        pygame.draw.rect(screen, (255, 255, 255), (x * cell_size, y * cell_size, cell_size, cell_size))
        head_x, head_y = snake[0]
        pygame.draw.circle(screen, (0,0,0), (head_x * cell_size + 6, head_y * cell_size + 6), 2)
        pygame.draw.circle(screen, (0,0,0), (head_x * cell_size + 14, head_y * cell_size + 6), 2)
        food_x, food_y = food
        pygame.draw.rect(screen, (255, 0, 0), (food_x * cell_size, food_y * cell_size, cell_size, cell_size))

def new_food_position():
    while True:
        x = random.randint(0, 29)
        y = random.randint(0, 19)
        new_pos = (x, y)
        
        if new_pos not in snake:
            return new_pos

def game_over_screen(screen, score):
    gameOverSound.play()
    font = pygame.font.SysFont(None, 50)
    text = font.render(f"Game Over! Score: {score}", True, (255, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (150, 180))
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
    pygame.quit()

def move_snake():
    global running
    global food
    
    head_x, head_y = snake[0]
    
    if direction == "RIGHT":
        new_head = (head_x + 1, head_y)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    elif direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)
    
    new_x, new_y = new_head

    ate_food = False
    if new_head == food:
        food = new_food_position()
        ate_food = True
        eat_sound.play()
        global score
        score += 1
    
    if new_x < 0 or new_x > 29 or new_y < 0 or new_y > 19:
        running = False
        return

    if new_head in snake:
        running = False
        return
    
    snake.insert(0, new_head)
    if not ate_food:
        snake.pop()
