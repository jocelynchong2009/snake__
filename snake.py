import pygame
import random
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20
pygame.font.init()
score_font = pygame.font.SysFont("consolas", 20)  # or any other font you'd like
score=0
white=(255,255,255)
red=(255,0,0)
pygame.init()
win=pygame.display.set_mode(width,height)
clock=pygame.time.Clock
snake_pos=[[width//2,height//2]]
snake_speed=[0,BLOCK_SIZE]
teleport_walls=True
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE ) * BLOCK_SIZE
        y = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE ) * BLOCK_SIZE
        food_pos=[x,y]
        if food_pos not in snake_pos:
            return food_pos
        if food_pos not in snake_pos:
            return food_pos
def draw_objects():
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    # Render the score
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))  
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    # Render the score
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))  
def draw_objects():
    win.fill((0,0,0))
    for pos in snake_pos:
        pygame.draw.rect(win,white,pygame.Rect(pos[0],pos[1],BLOCK_SIZE,BLOCK_SIZE))
        score_text=score_font.render(f)

