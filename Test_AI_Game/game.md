Для создания игры "Змейка" на Python, мы можем использовать библиотеку `pygame`, которая предоставляет функциональность для разработки игр. Следующие шаги помогут вам создать простую версию игры "Змейка".

### Шаги:

1. __Установка библиотеки `pygame`:__ Если у вас еще не установлена библиотека `pygame`, вы можете установить её с помощью pip:

   ```sh
   pip install pygame
   ```

2. __Создание основного файла игры:__ Создайте новый файл, например `snake_game.py`.

3. __Написание кода для игры:__ Откройте файл `snake_game.py` и вставьте следующий код:

   ```python
   import pygame
   import time
   import random

   # Инициализация pygame
   pygame.init()

   # Определение цветов
   white = (255, 255, 255)
   yellow = (255, 255, 102)
   black = (0, 0, 0)
   red = (213, 50, 80)
   green = (0, 255, 0)
   blue = (50, 153, 213)

   # Определение размеров экрана
   dis_width = 800
   dis_height = 600

   # Создание экрана
   dis = pygame.display.set_mode((dis_width, dis_height))
   pygame.display.set_caption('Змейка')

   # Определение шрифта
   font_style = pygame.font.SysFont(None, 50)
   score_font = pygame.font.SysFont(None, 35)

   def our_snake(snake_block, snake_list):
       for x in snake_list:
           pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

   def message(msg, color):
       mesg = font_style.render(msg, True, color)
       dis.blit(mesg, [dis_width / 6, dis_height / 3])

   def gameLoop():
       game_over = False
       game_close = False

       x1 = dis_width / 2
       y1 = dis_height / 2

       x1_change = 0
       y1_change = 0

       snake_List = []
       Length_of_snake = 1

       foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
       foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

       while not game_over:

           while game_close == True:
               dis.fill(blue)
               message("Вы проиграли! Нажмите Q для выхода или C для продолжения", red)
               pygame.display.update()

               for event in pygame.event.get():
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_q:
                           game_over = True
                           game_close = False
                       if event.key == pygame.K_c:
                           gameLoop()

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   game_over = True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_LEFT:
                       x1_change = -snake_block
                       y1_change = 0
                   elif event.key == pygame.K_RIGHT:
                       x1_change = snake_block
                       y1_change = 0
                   elif event.key == pygame.K_UP:
                       y1_change = -snake_block
                       x1_change = 0
                   elif event.key == pygame.K_DOWN:
                       y1_change = snake_block
                       x1_change = 0

           if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
               game_close = True
           x1 += x1_change
           y1 += y1_change
           dis.fill(blue)
           pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
           snake_Head = []
           snake_Head.append(x1)
           snake_Head.append(y1)
           snake_List.append(snake_Head)
           if len(snake_List) > Length_of_snake:
               del snake_List[0]

           for x in snake_List[:-1]:
               if x == snake_Head:
                   game_close = True

           our_snake(snake_block, snake_List)

           pygame.display.update()

           if x1 == foodx and y1 == foody:
               foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
               foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
               Length_of_snake += 1

           clock = pygame.time.Clock()
           clock.tick(15)

       pygame.quit()
       quit()

   gameLoop()
   ```

4. __Запуск игры:__ Запустите файл `snake_game.py` с помощью Python:

   ```sh
   python snake_game.py
   ```

Этот код создает базовую версию игры "Змейка". Вы можете улучшить игру, добавив дополнительные функции, такие как счет, уровни сложности, звуковые эффекты и т.д.

### Важные моменты:

- `pygame.init()` инициализирует все модули pygame.
- `pygame.display.set_mode((dis_width, dis_height))` создает окно игры.
- `pygame.font.SysFont(None, 50)` и `pygame.font.SysFont(None, 35)` используются для отображения текста.
- `our_snake(snake_block, snake_list)` рисует змейку на экране.
- `message(msg, color)` отображает сообщение на экране.
- `gameLoop()` содержит основной цикл игры.
