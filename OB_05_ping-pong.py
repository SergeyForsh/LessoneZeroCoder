import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Частота обновления
FPS = 60
clock = pygame.time.Clock()

# Параметры ракеток
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5

# Параметры мяча
BALL_SIZE = 15
BALL_SPEED = 5

# Создание объектов
left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Скорость мяча
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Счет игроков
left_score = 0
right_score = 0

# Шрифт для текста
font = pygame.font.Font(None, 74)

def draw_objects():
    """Отрисовка игровых объектов на экране."""
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, WHITE, left_paddle)
    pygame.draw.rect(SCREEN, WHITE, right_paddle)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Отображение счета
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    SCREEN.blit(left_text, (WIDTH // 4, 20))
    SCREEN.blit(right_text, (WIDTH * 3 // 4, 20))


def handle_paddle_movement(keys):
    """Обработка движения ракеток."""
    # Левая ракетка
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Правая ракетка
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    handle_paddle_movement(keys)

    # Движение мяча
    ball.x += ball_dx
    ball.y += ball_dy

    # Отражение мяча от верхней и нижней границ
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Отражение мяча от ракеток
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx *= -1

    # Проверка на гол
    if ball.left <= 0:
        right_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1
    if ball.right >= WIDTH:
        left_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_dx *= -1

    # Отрисовка объектов и обновление экрана
    draw_objects()
    pygame.display.flip()

    # Установка частоты обновления
    clock.tick(FPS)
