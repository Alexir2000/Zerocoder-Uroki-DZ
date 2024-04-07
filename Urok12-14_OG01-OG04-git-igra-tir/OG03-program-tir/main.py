import pygame
import random

pygame.init()

font = pygame.font.Font(None, 36) # None - используется дефолтный шрифт, 36 - размер шрифта

def display_text():
    text1 = f"Попыток: {k_pokaz}"
    text2 = f"Попаданий: {k_popal}"
    pos1 = (10, 10)
    pos2 = (10, 50)
    text_surface1 = font.render(text1, True, (255, 255, 255))  # создаем поверхность текста Белый цвет
    text_surface2 = font.render(text2, True, (255, 255, 255))
    screen.blit(text_surface1, pos1)  # отображаем текст на экране
    screen.blit(text_surface2, pos2)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(" Игра ТИР")

icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target_img.png")
target_width = 80
target_height = 80

target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

running = True

k_pokaz = 0
k_popal = 0

# инициализация
screen.fill(color)
display_text()
screen.blit(target_img, (target_x, target_y))
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            k_pokaz += 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                k_popal += 1
        screen.fill(color)
        display_text()
        screen.blit(target_img, (target_x, target_y))
        pygame.display.update()

pygame.quit()

