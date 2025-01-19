import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Частота обновления
FPS = 10
clock = pygame.time.Clock()

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Начальные параметры змейки
snake = [pygame.Rect(WIDTH // 2, HEIGHT // 2, CELL_SIZE, CELL_SIZE)]
snake_dir = RIGHT

def spawn_food():
    """Генерация еды в случайной позиции."""
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    return pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

# Создание первой еды
food = spawn_food()

# Счет игрока
score = 0
font = pygame.font.Font(None, 36)

def draw_objects():
    """Отрисовка змейки, еды и счета."""
    SCREEN.fill(BLACK)

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(SCREEN, GREEN, segment)

    # Отрисовка еды
    pygame.draw.rect(SCREEN, RED, food)

    # Отображение счета
    score_text = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление направлением змейки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != DOWN:
        snake_dir = UP
    if keys[pygame.K_DOWN] and snake_dir != UP:
        snake_dir = DOWN
    if keys[pygame.K_LEFT] and snake_dir != RIGHT:
        snake_dir = LEFT
    if keys[pygame.K_RIGHT] and snake_dir != LEFT:
        snake_dir = RIGHT

    # Перемещение змейки
    head = snake[0]
    new_head = head.move(snake_dir[0] * CELL_SIZE, snake_dir[1] * CELL_SIZE)

    # Проверка столкновения с границами
    if new_head.left < 0 or new_head.right > WIDTH or new_head.top < 0 or new_head.bottom > HEIGHT:
        break  # Конец игры

    # Проверка столкновения с собой
    if new_head in snake:
        break  # Конец игры

    # Добавление нового сегмента в голову змейки
    snake.insert(0, new_head)

    # Проверка съедения еды
    if new_head == food:
        score += 1
        food = spawn_food()
    else:
        snake.pop()  # Удаление хвоста, если еда не съедена

    # Отрисовка объектов и обновление экрана
    draw_objects()
    pygame.display.flip()

    # Установка частоты обновления
    clock.tick(FPS)

# Отображение конечного сообщения
SCREEN.fill(BLACK)
game_over_text = font.render("Game Over!", True, WHITE)
final_score_text = font.render(f"Final Score: {score}", True, WHITE)
SCREEN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
SCREEN.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()

# Задержка перед выходом
pygame.time.wait(3000)
pygame.quit()
