import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 800
CELL_SIZE = 20
COLUMNS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тетрис")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
COLORS = [
    (0, 255, 255),  # Циан
    (255, 255, 0),  # Желтый
    (128, 0, 128),  # Фиолетовый
    (0, 0, 255),    # Синий
    (255, 165, 0),  # Оранжевый
    (0, 255, 0),    # Зеленый
    (255, 0, 0),    # Красный
]

# Частота обновления
FPS = 60
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 500  # Скорость падения фигуры в миллисекундах

# Фигуры тетриса
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
]

class Tetris:
    def __init__(self):
        self.board = [[0] * COLUMNS for _ in range(ROWS)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.piece_position = [0, COLUMNS // 2 - len(self.current_piece[0]) // 2]
        self.score = 0

    def new_piece(self):
        """Создание новой фигуры."""
        shape = random.choice(SHAPES)
        color = random.randint(1, len(COLORS))
        return [[color if cell else 0 for cell in row] for row in shape]

    def draw_board(self):
        """Отрисовка игрового поля."""
        SCREEN.fill(BLACK)
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(SCREEN, COLORS[cell - 1], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        SCREEN, COLORS[cell - 1],
                        ((self.piece_position[1] + x) * CELL_SIZE, (self.piece_position[0] + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    )

    def move_piece(self, dx, dy):
        """Перемещение фигуры."""
        new_position = [self.piece_position[0] + dy, self.piece_position[1] + dx]
        if not self.check_collision(self.current_piece, new_position):
            self.piece_position = new_position

    def rotate_piece(self):
        """Поворот фигуры."""
        rotated = [list(row) for row in zip(*self.current_piece[::-1])]
        if not self.check_collision(rotated, self.piece_position):
            self.current_piece = rotated

    def check_collision(self, piece, position):
        """Проверка столкновений с границами и другими фигурами."""
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = position[1] + x
                    new_y = position[0] + y
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                        return True
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return True
        return False

    def freeze_piece(self):
        """Закрепление фигуры на игровом поле."""
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.piece_position[0] + y][self.piece_position[1] + x] = cell
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        self.piece_position = [0, COLUMNS // 2 - len(self.current_piece[0]) // 2]
        if self.check_collision(self.current_piece, self.piece_position):
            self.game_over()

    def clear_lines(self):
        """Удаление заполненных линий."""
        self.board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = ROWS - len(self.board)
        self.score += lines_cleared
        self.board = [[0] * COLUMNS for _ in range(lines_cleared)] + self.board

    def game_over(self):
        """Завершение игры."""
        pygame.quit()
        sys.exit()

# Основной игровой цикл
game = Tetris()
last_fall_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        game.move_piece(-1, 0)
    if keys[pygame.K_RIGHT]:
        game.move_piece(1, 0)
    if keys[pygame.K_DOWN]:
        game.move_piece(0, 1)
    if keys[pygame.K_UP]:
        game.rotate_piece()

    # Падение фигуры
    current_time = pygame.time.get_ticks()
    if current_time - last_fall_time > fall_speed:
        if game.check_collision(game.current_piece, [game.piece_position[0] + 1, game.piece_position[1]]):
            game.freeze_piece()
        else:
            game.move_piece(0, 1)
        last_fall_time = current_time

    game.draw_board()
    pygame.display.flip()
    clock.tick(FPS)
