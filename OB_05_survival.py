import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра на выживание")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Частота обновления
FPS = 60
clock = pygame.time.Clock()

# Параметры игрока
PLAYER_SIZE = 20
PLAYER_SPEED = 5
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)

# Параметры врагов
ENEMY_SIZE = 20
ENEMY_SPEED = 3
ENEMY_SPAWN_RATE = 30  # Количество кадров между появлением врагов

enemies = []  # Список врагов
frames_since_last_spawn = 0

# Счет игрока
score = 0
font = pygame.font.Font(None, 36)

def draw_objects():
    """Отрисовка объектов на экране."""
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, GREEN, player)
    for enemy in enemies:
        pygame.draw.rect(SCREEN, RED, enemy)

    # Отображение счета
    score_text = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

def move_enemies():
    """Движение врагов вниз по экрану."""
    global enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
    enemies = [enemy for enemy in enemies if enemy.top < HEIGHT]  # Удаление врагов за экраном

def spawn_enemy():
    """Создание нового врага."""
    x_pos = random.randint(0, WIDTH - ENEMY_SIZE)
    new_enemy = pygame.Rect(x_pos, 0, ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(new_enemy)

def check_collision():
    """Проверка столкновений игрока с врагами."""
    for enemy in enemies:
        if player.colliderect(enemy):
            return True
    return False

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PLAYER_SPEED

    # Обновление врагов
    frames_since_last_spawn += 1
    if frames_since_last_spawn >= ENEMY_SPAWN_RATE:
        spawn_enemy()
        frames_since_last_spawn = 0

    move_enemies()

    # Проверка столкновений
    if check_collision():
        break  # Конец игры

    # Увеличение счета
    score += 1

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
