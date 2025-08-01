import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/tir.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/monster.png")

target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True

# Инициализация переменных для таймера и счёта
game_time = 30  # Время игры в секундах
start_time = pygame.time.get_ticks()
score = 0

# Шрифты для отображения текста
font = pygame.font.Font(None, 36)

while running:
    # Проверяем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Очистка экрана
    screen.fill(color)

    # Таймер
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    if elapsed_time >= game_time:
        print(f"Время вышло! Ваш счёт: {score}")
        running = False
    else:
        time_left = game_time - elapsed_time

    # Отрисовка мишени
    screen.blit(target_image, (target_x, target_y))

    # Отрисовка счёта и времени
    score_text = font.render(f"Счёт: {score}", True, (255, 255, 255))
    time_text = font.render(f"Время: {time_left}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    # Обновление экрана
    pygame.display.update()

pygame.quit()

#Оценка сложности алгоритма в вашей игре "Тир"
#Сложность алгоритма: O(1) – константное время
#Основной алгоритм в вашей игре (проверка попадания, перемещение мишени, отрисовка)
# выполняется за константное время на каждом кадре, так как:
#Проверка клика (if target_x < mouse_x < target_x + target_width ...) – это несколько
# сравнений (O(1)).
#Рендеринг (screen.blit) и генерация случайных чисел (random.randint) тоже работают за O(1).
#Итоговая сложность не зависит от размера входных данных (например, количества мишеней или
# разрешения экрана), поэтому алгоритм считается очень простым и эффективным для данной задачи.
#Итоговая оценка
#✅ Простота: 10/10
#✅ Эффективность: 10/10
#✅ Оптимизация: Подходит для реального использования.
#Код отлично структурирован для начинающих. Для расширения функционала можно добавить
# систему уровней или сохранение рекордов.