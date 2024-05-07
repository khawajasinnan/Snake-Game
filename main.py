import pygame
import random

WHITE = (255,255,255)
BLACK = (20,20,20)
GREEN = (0,255,0)
RED = (255,0,0)

WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 18
VEL = PLAYER_SIZE = 10

pygame.font.init()
SCORE_FONT = pygame.font.SysFont('comicsans', 20)

random_x = random.randint(0,39) * PLAYER_SIZE
random_y = random.randint(0,39) * PLAYER_SIZE

SNAKE_GROW = pygame.USEREVENT + 1
GAME_OVER = pygame.USEREVENT + 2

pygame.display.set_caption("Snake")

def draw_board(apple, snake_list, score):
  WIN.fill(BLACK)
  pygame.draw.rect(WIN, RED, apple)
  for x in snake_list:
    pygame.draw.rect(WIN, GREEN, [x[0], x[1], PLAYER_SIZE, PLAYER_SIZE])
  score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
  WIN.blit(score_text, (10,10))
  pygame.display.update() # KEEP AT BOTTOM

def handle_movement(player, direction):
  if direction == "UP":
    player.y -= VEL
  if direction == "DOWN":
    player.y += VEL
  if direction == "LEFT":
    player.x -= VEL
  if direction == "RIGHT":
    player.x += VEL

def handle_eating(snake_list, apple):
  if snake_list[-1] == [apple.x, apple.y]:

      apple.x = random.randint(0,39) * PLAYER_SIZE
      apple.y = random.randint(0,39) * PLAYER_SIZE

      pygame.event.post(pygame.event.Event(SNAKE_GROW))

def game_over():
  print ("GAME OVER")
  pygame.event.post(pygame.event.Event(GAME_OVER))
  WIN.fill(WHITE)
  pygame.display.update()

def main():

  clock = pygame.time.Clock()
  player = pygame.Rect(100, 100, PLAYER_SIZE, PLAYER_SIZE)
  apple = pygame.Rect(random_x, random_y, PLAYER_SIZE, PLAYER_SIZE)
  score = 0
  run = True
  direction = ""
  snake_list = []
  FPS = 10
  snake_length = 1
  while run:

    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if event.type == GAME_OVER:
        run = False

      if event.type == SNAKE_GROW:
        score += 1
        print ("Score: " + str(score))
        snake_length += 1

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP and direction != "DOWN":
            direction = "UP"
          elif event.key == pygame.K_DOWN and direction != "UP":
            direction = "DOWN"
          elif event.key == pygame.K_LEFT and direction != "RIGHT":
            direction = "LEFT"
          elif event.key == pygame.K_RIGHT and direction != "LEFT":
            direction = "RIGHT"

    if player.x < 0 or player.x + PLAYER_SIZE > WIDTH:
      game_over()

    if player.y < 0 or player.y + PLAYER_SIZE > HEIGHT:
      game_over()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LSHIFT]:
      FPS = 30
    else:
      FPS = 10
    snake_head = []
    snake_head.append(player.x)
    snake_head.append(player.y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
      del snake_list[0]
    if snake_list.count(snake_list[-1]) > 1:
      print ("CULPRIT")
    handle_eating(snake_list, apple)
    handle_movement(player,direction)
    draw_board(apple, snake_list, score)

if __name__ == "__main__":
  main()
