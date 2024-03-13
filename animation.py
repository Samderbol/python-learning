import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口大小
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
bg = (255, 255, 255)
# 创建窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monkey get Banana Animation")

# 加载猴子、箱子和香蕉的图片
MONKEY_IMG = pygame.image.load("monkey.png")
BOX_IMG = pygame.image.load("box.png")
BANANA_IMG = pygame.image.load("banana.png")

# 猴子、箱子和香蕉的初始位置
monkey_x, monkey_y = 1000, 800   
box_x, box_y = 200, 800
#默认位置参数为猴子在箱子右侧

#monkey_x和box_x二者建议取值(100,1000),X越大位置越往右
banana_x, banana_y = 1000, 200

screen.fill(bg)
# 动画主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 绘制猴子、箱子和香蕉
    screen.blit(MONKEY_IMG, (monkey_x, monkey_y))
    screen.blit(BOX_IMG, (box_x, box_y))
    screen.blit(BANANA_IMG, (banana_x, banana_y))

    # 更新屏幕
   
    pygame.display.flip()

    # 控制猴子移动
    if monkey_x <= banana_x and box_x!= banana_x :
        if monkey_x <= box_x:
         if monkey_x < box_x:
          monkey_x += 1

         elif monkey_x == box_x:
           monkey_x += 1
           box_x +=1

        elif monkey_x >= box_x:
          monkey_x -= 1
          if monkey_x == box_x:
             monkey_x += 1
             box_x +=1
    
        else:
         monkey_x += 1
         box_x +=1

    else:
       if monkey_x <= banana_x and monkey_y >=banana_y:
        monkey_x += 1
       else:
        if monkey_y >= banana_y-100:
         monkey_y -=1
        else:
         monkey_y =banana_y-100

# 退出动画
pygame.quit()
sys.exit()
