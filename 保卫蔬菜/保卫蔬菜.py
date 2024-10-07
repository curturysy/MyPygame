
# 导入各种模块
import pygame as pyg
import random,sys,math

pyg.display.set_caption("保卫蔬菜")  # 窗口名字

# 初始化
pyg.init()
pyg.mixer.init()

# 定义窗口的宽高
WIN_WIDTH = 1366
WIN_HEIGHT = 688

screen = pyg.display.set_mode([WIN_WIDTH, WIN_HEIGHT])  # 设置窗口的宽和高

# 各种图片

backg = pyg.image.load('image/background.png').convert_alpha()  # 导入背景图片

loading_image = pyg.image.load('image/loading.png').convert_alpha()  # 导入背景图片

black_image = pyg.image.load('image/黑幕.png').convert_alpha()  # 导入背景图片

choose_image = pyg.image.load('image/choose.png').convert_alpha()  # 导入背景图片

start_ui = pyg.image.load('image/start_ui.png').convert_alpha()  # 开始游戏界面

boy = pyg.image.load('image/boy.png').convert_alpha()  # 主角图片

angry_boy = pyg.image.load('image/angry_boy.png').convert_alpha()  # 主角图片

image_fly = pyg.image.load('image/fly.png').convert_alpha()  # 苍蝇图片
image_blue_fly = pyg.image.load('image/blue_fly.png').convert_alpha()  # 蓝色苍蝇图片

image_ladybug = pyg.image.load('image/ladybug.png').convert_alpha()  # 瓢虫图片
image_blue_ladybug = pyg.image.load('image/blue_ladybug.png').convert_alpha()  # 蓝色瓢虫图片

image_lazer = pyg.image.load('image/lazer.png').convert_alpha()  # 激光图片

image_energy = pyg.image.load('image/energy.png').convert_alpha()  # 能量图片

image_blue = pyg.image.load('image/blue.png').convert_alpha()  # 蓝色粒子效果图片

image_red = pyg.image.load('image/red.png').convert_alpha()  # 红字粒子效果图片

hit_show_image = pyg.image.load('image/hit_show.png').convert_alpha()  # 打击效果

hammer0 = pyg.image.load('image/hammer0.png').convert_alpha()  # 锤子图片1

hammer1 = pyg.image.load('image/hammer1.png').convert_alpha()  # 锤子图片2

hit_range_image = pyg.image.load('image/hit_range.png').convert_alpha()

vegetable = pyg.image.load('image/new_v.png').convert_alpha()  # 蔬菜图片

line_image = pyg.image.load('image/line.png').convert_alpha() #判定线图片

explain = pyg.image.load('image/explain.png')  # 说明界面图片

next_explain = pyg.image.load('image/next.png')  # 说明界面图片

image_over = pyg.image.load('image/over.png')  # 结束界面图片

stop_image = pyg.image.load('image/stop.png')  # 暂停界面图片

broad_image = pyg.image.load('image/broad.png')  # 暂停界面图片

three = pyg.image.load('image/3.png') 

two = pyg.image.load('image/2.png')

one = pyg.image.load('image/1.png')

gameIcon = pyg.image.load('image/icon.jpg')  # 游戏图标

pyg.display.set_icon(gameIcon)

hit = pyg.mixer.Sound('sound/hit.wav')

eat = pyg.mixer.Sound('sound/eat.wav')

click = pyg.mixer.Sound('sound/click.wav')  # 创建点击按钮触发的声音

lazer_sound = pyg.mixer.Sound('sound/lazer3.wav')  # 创建点击按钮触发的声音

attack = pyg.mixer.Sound('sound/attack2.mp3')

# 创建大厅BGM
def hub_BGM():
    pyg.mixer.music.load('sound/hub_BGM.mp3')
    pyg.mixer.music.play(-1)
    pyg.mixer.music.set_volume(0.2)

def fight_BGM():
    pyg.mixer.music.load('sound/BGM.mp3')
    pyg.mixer.music.play(-1)
    pyg.mixer.music.set_volume(0.5)

hub_BGM()

boy_x = 180
boy_y = 290
game_time = 0  # 游戏时间,不断增加

# 创建颜色的RGB值，方便后期调用
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# 定义分数
score = 0  # 消灭虫子的得分
kill = 0  # 击杀害虫数
last_score = None
loss_score = None
best_score_txt = open('data/best_score.txt', 'r')
best_score = best_score_txt.read()
# 玩家得分所对应的等级
rank = None
loss_score_change = 0
live = 3  # 生命值，虫子吃了蔬菜生命值会减少

#continue
continue_game = 'no'

global run
run = True
over = False

# 创建游戏图标
pyg.display.set_icon(gameIcon)

def hit_sound():
    hit.set_volume(0.2)
    hit.play()

def attack_sound():
    attack.set_volume(0.8)
    attack.play()

def eat_sound():
    eat.set_volume(0.4)
    eat.play()

def click_sound():
    click.set_volume(0.2)
    click.play()

# 计分系统
def Score(score):
    font = pyg.font.Font('font/再见旧时光.ttf', 30)
    text = font.render("分数:" + str(score) + '     剩余蔬菜:' + str(live) + '     击杀害虫数:' + str(kill), True, BLACK)
    screen.blit(text, (WIN_WIDTH / 3.25, 0))

def game_over1():
    over = True
    time = 0
    font = pyg.font.Font('font/再见旧时光.ttf', 30)
    pyg.mixer.music.fadeout(1500)
    while over:
        time += 1
        if time < 100:
            text = font.render(str(random.randint(1, 10000)), True, RED)
        if time >= 100:
            over = False
            game_over2()
        screen.blit(image_over, (325, 100))
        screen.blit(text, (WIN_WIDTH / 2.6, 185))
        pyg.display.flip()
        
def game_over2():
    over = True
    time = 0
    font = pyg.font.Font('font/再见旧时光.ttf', 30)
    text_before1 = font.render(str(score), True, RED)
    while over:
        time += 1
        if time < 100:
            text = font.render(str(random.randint(1, 10000)), True, RED)
        if time >= 100:
            text = font.render(str(kill), True, RED)
            over = False
            game_over3()
        screen.blit(image_over, (325, 100))
        screen.blit(text_before1, (WIN_WIDTH / 2.6, 185))
        screen.blit(text, (WIN_WIDTH / 2.8, 257))
        pyg.display.flip()

def game_over3():
    over = True
    time = 0
    font = pyg.font.Font('font/再见旧时光.ttf', 30)
    text_before1 = font.render(str(score), True, RED)
    text_before2 = font.render(str(kill), True, RED)
    while over:
        time += 1
        if time < 50:
            text = font.render(str(random.randint(1, 10000)), True, RED)
        if time >= 50:
            text = font.render(str(last_score), True, RED)
            over = False
            game_over4()
        screen.blit(image_over, (325, 100))
        screen.blit(text_before1, (WIN_WIDTH / 2.6, 185))
        screen.blit(text_before2, (WIN_WIDTH / 2.8, 257))
        screen.blit(text, (WIN_WIDTH / 2.6, 324))
        pyg.display.flip()

def game_over4():
    global number, hit_number
    hit_lv = hit_number/number
    over = True
    time = 0
    font = pyg.font.Font('font/再见旧时光.ttf', 30)
    font2 = pyg.font.Font('font/再见旧时光.ttf', 30)
    text_before1 = font.render(str(score), True, RED)
    text_before2 = font.render(str(kill), True, RED)
    text_before3 = font.render(str(last_score), True, RED)
    while over:
        time += 1
        if time < 50:
            text = font.render(str(random.randint(1, 10000)), True, RED)
        if time >= 50:
            text = font2.render(str(round(hit_lv, 2)), True, RED)
            over = False
            game_over5()
        screen.blit(image_over, (325, 100))
        screen.blit(text_before1, (WIN_WIDTH / 2.6, 185))
        screen.blit(text_before2, (WIN_WIDTH / 2.8, 257))
        screen.blit(text_before3, (WIN_WIDTH / 2.6, 324))
        screen.blit(text, (WIN_WIDTH / 2.8, 390))  # (WIN_WIDTH / 1.58, 190)
        pyg.display.flip()

def game_over5():
    global number, hit_number
    hit_lv = hit_number/number
    over = True
    time = 0
    font = pyg.font.Font('font/LEVIBRUSH.ttf', 100)
    font2 = pyg.font.Font('font/再见旧时光.ttf', 30)
    text_before1 = font2.render(str(score), True, RED)
    text_before2 = font2.render(str(kill), True, RED)
    text_before3 = font2.render(str(last_score), True, RED)
    text_before4 = font2.render(str(round(hit_lv, 2)), True, RED)
    while over:
        time += 1
        if time < 100:
            text = font2.render(str(random.randint(1,999)), True, RED)
        if time >= 100:
            text = font2.render(str(best_score), True, RED)
        if time >= 110:
            over = False
            game_over6()
        screen.blit(image_over, (325, 100))
        screen.blit(text_before1, (WIN_WIDTH / 2.6, 185))
        screen.blit(text_before2, (WIN_WIDTH / 2.8, 257))
        screen.blit(text_before3, (WIN_WIDTH / 2.6, 324))
        screen.blit(text_before4, (WIN_WIDTH / 2.8, 390))
        screen.blit(text, (WIN_WIDTH / 1.58, 190))  # (WIN_WIDTH / 2.8, 390)
        pyg.display.flip()

def game_over6():
    global number,hit_number
    hit_lv = hit_number/number
    over = True
    time = 0
    font = pyg.font.Font('font/LEVIBRUSH.ttf', 100)
    font2 = pyg.font.Font('font/再见旧时光.ttf', 30)
    text_before1 = font2.render(str(score), True, RED)
    text_before2 = font2.render(str(kill), True, RED)
    text_before3 = font2.render(str(last_score), True, RED)
    text_before4 = font2.render(str(best_score), True, RED)
    text_before5 = font2.render(str(round(hit_lv,2)), True, RED)
    while over:
        time += 1
        if time < 100:
            text = font.render(str(random.randint(1, 999)), True, RED)
        if time >= 100:
            text = font.render(str(rank), True, RED)
        if time >= 110:
            over = False
            game_over7()
        screen.blit(image_over, (325, 100))
        screen.blit(text_before1, (WIN_WIDTH / 2.6, 185))
        screen.blit(text_before2, (WIN_WIDTH / 2.8, 257))
        screen.blit(text_before3, (WIN_WIDTH / 2.6, 324))
        screen.blit(text_before4, (WIN_WIDTH / 1.58, 190))
        screen.blit(text_before5, (WIN_WIDTH / 2.8, 390))
        screen.blit(text, (WIN_WIDTH / 1.73, 240))
        pyg.display.flip()

def game_over7():
    over = True
    over_again_button = Button('重玩', RED, None, 350, centered_x=True)  # 创建重新开始按钮
    over_return_button = Button('返回', RED, None, 400, centered_x=True)  # 创建游戏说明按钮
    over_exit_button = Button('退出', RED, None, 450, centered_x=True)  # 创建退出按钮
    while over:
        global remake, last_score_remake
        if over_again_button.check_click(pyg.mouse.get_pos()):
            over_again_button = Button('重玩', RED, None, 350, centered_x=True)
        else:
            over_again_button = Button('重玩', BLACK, None, 350, centered_x=True)
        if over_return_button.check_click(pyg.mouse.get_pos()):
            over_return_button = Button('返回', RED, None, 400, centered_x=True)
        else:
            over_return_button = Button(
                '返回', BLACK, None, 400, centered_x=True)
        if over_exit_button.check_click(pyg.mouse.get_pos()):
            over_exit_button = Button('退出游戏', RED, None, 450, centered_x=True)
        else:
            over_exit_button = Button(
                '退出游戏', BLACK, None, 450, centered_x=True)

        over_again_button.display()
        over_return_button.display()
        over_exit_button.display()
        pyg.display.update()

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                raise SystemExit
        if pyg.mouse.get_pressed()[0]:
            if over_again_button.check_click(pyg.mouse.get_pos()):
                click_sound()
                remake = 1
                last_score_remake = 1  # 重置上局积分
                over = False
            if over_return_button.check_click(pyg.mouse.get_pos()):
                hub_BGM()
                click_sound()
                remake = 1
                last_score_remake = 1  # 重置上局积分
                starting_screen()  # 回到主界面
                over = False
            if over_exit_button.check_click(pyg.mouse.get_pos()):  # 退出游戏
                pyg.quit()
                sys.exit()

# 创建锤子类
class Hammer(pyg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.image = hit_range_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = 0 
    def update(self):
        self.time += 1
        if self.time > 5:
            self.kill()

        #self.location = [self.rect.x, self.rect.y]
        #screen.blit(self.image, self.location)

#判定线
class Line(pyg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.image = line_image
        self.rect = self.image.get_rect()
        self.rect.x = -50
        self.rect.y = 0

class Blue_red(pyg.sprite.Sprite):  #粒子效果
    #初始化
    def __init__(self, x, y,c):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.c = c
        if self.c == 'red':
            self.image = image_red
        if self.c == 'blue':
            self.image = image_blue#C
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = random.randint(-1, 6)
        self.y_speed = random.randint(-3,3)
        self.y_add_speed = 0.1
        self.time = 0
    #行为

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.y_speed += self.y_add_speed
        self.time += 1
        if self.time >= 15:
            self.kill()
        #绘制
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)

#pyg.draw.circle(screen,color,position,radius,width)
'''screen:画布
color:指定的颜色（可以是pygame常量也可以是RGB）
position:位置
radius:直径
width:线条宽度（如果想要画实心圆就把它设为radius）'''

class Hit_show(pyg.sprite.Sprite):  #打击特效
    #初始化
    def __init__(self, x, y):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.px = x
        self.py = y
        #self.image = pyg.draw.circle(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(self.px,self.py),random.randint(6,9),random.randint(2,3))
        self.image = hit_show_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = random.randint(-7,7)
        self.y_speed = random.randint(-7,7)
        self.time = 0
    #行为

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.time += 1
        if self.time >= 15:
            self.kill()
        #绘制
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)

# 创建苍蝇类
class Fly(pyg.sprite.Sprite):
    y_speed = 0
    dead_x_speed = 5
    dead_y_speed = 0
    add_y_speed = 0.35  # 重力加速度
    def __init__(self,c):
        super(Fly, self).__init__()
        pyg.sprite.Sprite.__init__(self)
        self.image = image_fly
        self.rect = self.image.get_rect()
        self.y_list = [115, 305, 500]
        self.rect.y = random.choice(self.y_list)
        self.rect.x = 1500
        self.c = c
        self.x_speed = random.randint(-10,-1)
        self.now = 'alive'
        self.playmusic = 1
        if self.c == 1:
            self.image = image_blue_fly
            self.x_speed = random.randint(-25,-15)
        else:
            self.image = image_fly

    def update(self):  # 苍蝇的生成和移动
        global score, all_stop, energy, hit_number
        if self.c == 1:
            self.blue_show = Blue_red(self.rect.x + 35, self.rect.y + 35,'blue')
            blue_list.add(self.blue_show)

        if remake == 1:
            self.kill()

        if all_stop == 'no':
            self.collide_sprite_lady = pyg.sprite.spritecollide(self,sprite_list_lady_hit,False)#苍蝇和瓢虫的碰撞
            self.collide_hammer = pyg.sprite.spritecollide(self,hammer_list,False)#苍蝇和锤子的碰撞
            self.collide_lazer = pyg.sprite.spritecollide(
                self, sprite_list_lazer, False)  # 激光和瓢虫的碰撞

            if self.now == 'alive':  # 如果苍蝇活了
                self.rect.x += self.x_speed
                #if self.c == 1:
                    #self.x_speed = random.randint(-30,5)
                    #self.x_speed = random.randint(-30, 5)


            if self.now == 'dead':  # 如果苍蝇死了
                hit_number += 1
                self.kill()
                score += self.Score_add
                self.y_speed = 0
                self.rect.y = random.choice(self.y_list)
                self.rect.x = 1400
                self.dead_x_speed = random.randint(-2, 8)
                self.now = 'alive'

            if (self.collide_lazer or self.collide_sprite_lady) and self.now == 'alive':  # 如果苍蝇被瓢虫或激光打到
                self.now = 'hit_dead'  # 切换状态
                energy += 1
                #hit_number += 1
                self.Score_add = random.randint(10, 50)
                self.Score_add_show = Score_add(self.rect.x, self.rect.y, self.Score_add)
                score_add_show_list.add(self.Score_add_show)
                if self.playmusic == 1:
                    score += self.Score_add
                    #hit_number += 1
                    self.playmusic = 0
                    hit_sound()
                    for self.i in range(random.randint(5, 10)):
                        self.hit = Hit_show(self.rect.x + 30, self.rect.y + 30)
                        blue_list.add(self.hit)

            if self.collide_hammer:  # 如果苍蝇被锤子打到
                energy += 1
                #hit_number += 1
                self.Score_add = random.randint(50, 60)
                self.Score_add_show = Score_add(self.rect.x, self.rect.y, self.Score_add)
                score_add_show_list.add(self.Score_add_show)
                for self.i in range(random.randint(5,10)):
                    self.hit = Hit_show(self.rect.x + 30,self.rect.y+ 30)
                    blue_list.add(self.hit)
                self.now = 'dead'

            if self.now == 'hit_dead':  # 苍蝇被瓢虫打死了            
                
                if self.rect.y <= 688:  # 如果苍蝇还在屏幕内
                    self.rect.x = self.rect.x + self.dead_x_speed  # 苍蝇的移动
                    self.y_speed = self.y_speed + self.add_y_speed
                    self.rect.y = self.rect.y + self.y_speed + self.dead_y_speed
                
                if self.rect.y > 688:  # 如果苍蝇在屏幕外
                    self.now = 'dead'  # 让它死
        
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)

# 创建瓢虫类
class Ladybug(pyg.sprite.Sprite):
    dead_x_speed = 5  # 向右的速度
    dead_y_speed = -8  # 向上的速度
    y_speed = 0 #y方向的速度
    add_y_speed = 0.25  # 重力加速度
    random_y_list = [1, 2]  # 这个东西决定瓢虫的去向
    random_y = random.choice(random_y_list)

    def __init__(self,c):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.image = image_ladybug
        self.rect = self.image.get_rect()
        self.rect.x = 1500
        self.y_list = [115, 310, 500]
        self.rect.y = random.choice(self.y_list)
        self.x_speed = random.randint(-15,-5)
        self.c = c
        self.now = 'alive'
        if self.c == 1:
            self.image = image_blue_ladybug
        else:
            self.image = image_ladybug

    def update(self):  # 瓢虫的生成和移动
        global score, all_stop, energy, hit_number
        if self.c == 1:
            self.blue_show = Blue_red(self.rect.x + 35, self.rect.y + 35,'blue')
            blue_list.add(self.blue_show)
        if remake == 1:
            self.kill()
        
        if all_stop == 'no':
            self.collide_hammer = pyg.sprite.spritecollide(
                self, hammer_list, False)  # 锤子和瓢虫的碰撞
            self.collide_sprite_fly = pyg.sprite.spritecollide(
                self, sprite_list_fly, False)  # 苍蝇和瓢虫的碰撞
            self.collide_lazer = pyg.sprite.spritecollide(self,sprite_list_lazer,False)#激光和瓢虫的碰撞

            if self.now == 'dead':# 如果瓢虫死了
                self.kill()
                hit_number += 1

            if self.collide_sprite_fly and self.now == 'hit_dead':  # 如果瓢虫碰到了苍蝇
                self.y_speed = 0
                
            # 如果瓢虫被锤子打到
            if (self.collide_lazer or self.collide_hammer) and (self.now == 'alive' or self.now == 'moving'):
                energy += 1
                #hit_number += 1
                self.now = 'hit_dead'
                self.Score_add = random.randint(100, 150)
                score += self.Score_add
                self.Score_add_show = Score_add(self.rect.x, self.rect.y, self.Score_add)
                score_add_show_list.add(self.Score_add_show)
                sprite_list_lady.remove(self)
                sprite_list_lady_hit.add(self)
                for self.i in range(random.randint(5, 10)):
                    self.hit = Hit_show(self.rect.x + 30, self.rect.y + 30)
                    blue_list.add(self.hit)

            if self.now == 'hit_dead':
                if self.rect.y <= 688:  # 如果瓢虫还在屏幕内
                    self.rect.x = self.rect.x + self.dead_x_speed  # 瓢虫的移动
                    self.y_speed = self.y_speed + self.add_y_speed
                    self.rect.y = self.rect.y + self.y_speed + self.dead_y_speed

                if self.rect.y > 688:  # 如果瓢虫还在屏幕外
                    self.now = 'dead'  # 让它死

            if self.now == 'alive':  # 如果瓢虫活了
                self.rect.x = self.rect.x + self.x_speed
                self.begin_y = self.rect.y
                if self.c == 1:
                    if self.rect.x >= 390:
                        self.up_down = random.randint(20, 60)
                else:
                    if self.rect.x >= 390:
                        self.up_down = random.randint(1,150)
                if self.up_down == 50 and self.rect.x > 270:
                    self.up_down = 50
                    self.now = 'moving'
                    self.ntr = random.randint(1,10)
                    if self.ntr == 5:
                        sprite_list_lady_hit.add(self)
                    else:
                        pass


            if self.now == 'moving':  # 如果瓢虫想动了
                self.x_speed = 0
                if self.random_y == -1:
                    self.random_y = random.choice(self.random_y_list)
                #瓢虫共有6种运动情况，因为共有3条线，在1条线上的时候有2种运动方法
                if self.random_y == 1 and self.begin_y == 115:  # 第1种情况
                    self.y_speed = 5
                    self.rect.y = self.rect.y + self.y_speed  # 瓢虫的上下运动
                    if self.rect.y == 310:#当运动结束时
                        sprite_list_lady_hit.remove(self)
                        self.begin_y = self.rect.y
                        self.y_speed = 0
                        self.random_y = -1
                        self.now = 'alive'
                        if self.c == 1:
                            self.x_speed = random.randint(-20, -7)
                        else:
                            self.x_speed = random.randint(-9, -1)

                elif self.random_y == 2 and self.begin_y == 115:  # 第2种情况
                    self.y_speed = 5
                    self.rect.y = self.rect.y + self.y_speed
                    if self.rect.y == 500:
                        sprite_list_lady_hit.remove(self)
                        self.begin_y = self.rect.y
                        self.y_speed = 0
                        self.random_y = -1
                        self.now = 'alive'
                        if self.c == 1:
                            self.x_speed = random.randint(-20, -7)
                        else:
                            self.x_speed = random.randint(-9, -1)
                if self.random_y == 1 and self.begin_y == 310:  # 第3种情况
                    self.y_speed = 5
                    self.rect.y = self.rect.y + self.y_speed
                    if self.rect.y == 500:
                        sprite_list_lady_hit.remove(self)
                        self.begin_y = self.rect.y
                        self.y_speed = 0
                        self.random_y = -1
                        self.now = 'alive'
                        if self.c == 1:
                            self.x_speed = random.randint(-20, -7)
                        else:
                            self.x_speed = random.randint(-9, -1)
                elif self.random_y == 2 and self.begin_y == 310:  # 第4种情况
                    self.y_speed = -5
                    self.rect.y = self.rect.y + self.y_speed
                    if self.rect.y == 115:
                        sprite_list_lady_hit.remove(self)
                        self.begin_y = self.rect.y
                        self.y_speed = 0
                        self.random_y = -1
                        self.now = 'alive'
                        if self.c == 1:
                            self.x_speed = random.randint(-20, -7)
                        else:
                            self.x_speed = random.randint(-9, -1)
                if self.random_y == 1 and self.begin_y == 500:  # 第5种情况
                    self.y_speed = -5
                    self.rect.y = self.rect.y + self.y_speed
                    if self.rect.y == 115:
                        sprite_list_lady_hit.remove(self)
                        self.begin_y = self.rect.y
                        self.y_speed = 0
                        self.random_y = -1
                        self.now = 'alive'
                        if self.c == 1:
                            self.x_speed = random.randint(-20, -7)
                        else:
                            self.x_speed = random.randint(-9, -1)
                elif self.random_y == 2 and self.begin_y == 500:  # 第6种情况
                    self.y_speed = -5
                    self.rect.y = self.rect.y + self.y_speed
                    if self.rect.y == 310:
                        sprite_list_lady_hit.remove(self)
                        self.begin_y = self.rect.y
                        self.y_speed = 0
                        self.random_y = -1
                        self.now = 'alive'
                        if self.c == 1:
                            self.x_speed = random.randint(-20, -7)
                        else:
                            self.x_speed = random.randint(-9, -1)
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)

# 创建蔬菜类
class Vegetable(pyg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.image = vegetable
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def spawn_stay(self):
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)


class Lazer1(pyg.sprite.Sprite):  # 激光1
    #初始化
    global boy_x,boy_y
    def __init__(self,move_y):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.image = image_lazer
        self.rect = self.image.get_rect()
        self.rect.x = boy_x + 70
        self.rect.y = boy_y + 30
        self.al_speed = 25  # 合速度
        self.gx = 1366
        self.gy = move_y
        self.d_to_mouse = math.sqrt(
            (self.rect.x - self.gx) ** 2 + (self.rect.y - self.gy) ** 2)  # 斜边
        self.d_to_mouse_x = self.gx - self.rect.x  # 对边
        self.d_to_mouse_y = self.gy - self.rect.y  # 邻边
        self.sin = self.d_to_mouse_x / self.d_to_mouse  # sin   
        self.cos = self.d_to_mouse_y / self.d_to_mouse  # cos
        self.y_speed = self.al_speed*self.cos  # y速度
        self.x_speed = self.al_speed*self.sin  # x速度
    #行为
    def update(self):
        #运动
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        #死亡
        if self.rect.y > 700 or self.rect.y < -20 or self.rect.x > 1400:
            self.kill()
        #绘制
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)

class Lazer2(pyg.sprite.Sprite):  #激光2
    #初始化
    def __init__(self, move_y):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.image = image_lazer
        self.rect = self.image.get_rect()
        self.rect.x = boy_x + 10
        self.rect.y = boy_y + 20
        self.al_speed = 25  # 合速度
        self.gx = 1366
        self.gy = move_y
        self.d_to_mouse = math.sqrt(
            (self.rect.x - self.gx) ** 2 + (self.rect.y - self.gy) ** 2)  # 斜边
        self.d_to_mouse_x = self.gx - self.rect.x  # 对边
        self.d_to_mouse_y = self.gy - self.rect.y  # 邻边
        self.sin = self.d_to_mouse_x / self.d_to_mouse  # sin
        self.cos = self.d_to_mouse_y / self.d_to_mouse  # cos
        self.y_speed = self.al_speed*self.cos  # y速度
        self.x_speed = self.al_speed*self.sin  # x速度
    #行为
    def update(self):
        #运动
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        #死亡
        if self.rect.y > 700 or self.rect.y < -30 or self.rect.x > 1400:
            self.kill()
        #绘制
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)


Score_add_text = pyg.font.Font('font/再见旧时光.ttf', 45)  # 得分显示字体
class Score_add(pyg.sprite.Sprite):  # 得分显示
    #初始化
    def __init__(self, x, y, Score_add):
        super().__init__()
        pyg.sprite.Sprite.__init__(self)
        self.Score_add_number = str(Score_add)
        self.image = Score_add_text.render(
            '+' + self.Score_add_number, True, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_speed = random.randint(-4, -2)
        self.x_speed = random.randint(-2, 2)
        self.y_add_speed = 0.3
    #行为

    def update(self):
        #运动
        self.y_speed += self.y_add_speed
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        #死亡
        if self.rect.y > 700:
            self.kill()
        #绘制
        self.location = [self.rect.x, self.rect.y]
        screen.blit(self.image, self.location)

# 创建按钮类
class Button(object):
    def __init__(self, text, color, x, y, **kwargs):
        self.surface = font1.render(text, True, color)
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        if 'centered_x' in kwargs and kwargs['centered_x']:
            self.x = WIN_WIDTH / 2.1
        else:
            self.x = x
        if 'centered_y' in kwargs and kwargs['cenntered_y']:
            self.y = WIN_HEIGHT / 3
        else:
            self.y = y

    def display(self):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):  # 0 是 x, 1 是 y
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False

# 定义游戏说明
def explain_button():
    image_number = 1
    show = True
    screen.blit(explain, (0, 0))  # 游戏说明界面
    back_button = Button('游戏说明', RED, None, 650, centered_x=True)
    next_button = Button('下一页', RED, None, 650, centered_x=True)
    while show:
        if back_button.check_click(pyg.mouse.get_pos()):
            back_button = Button('返回首页', RED,15 , 15)
        else:
            back_button = Button('返回首页', BLACK, 15, 15)

        if next_button.check_click(pyg.mouse.get_pos()):
            next_button = Button('下一页', RED, None, 640, centered_x=True)
        else:
            next_button = Button('下一页', BLACK, None, 640, centered_x=True)
        if image_number == 1:
            screen.blit(explain, (0, 0))  # 游戏说明界面
        if image_number == 2:
            screen.blit(next_explain, (0, 0))  # 游戏说明界面

        back_button.display()
        next_button.display()
        pyg.display.update()

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                raise SystemExit
            if pyg.mouse.get_pressed()[0]:
                if back_button.check_click(pyg.mouse.get_pos()):
                    click_sound()
                    show = False
                    starting_screen()

                if next_button.check_click(pyg.mouse.get_pos()):
                    click_sound()
                    image_number += 1
                    if image_number >= 3:
                        image_number = 1

def loading1():
    load = True
    time = 0
    while load:
        time += 1
        screen.blit(loading_image, (0, 0))
        pyg.display.flip()
        if time >= 1:
            load = False

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                raise SystemExit

def loading2():
    load = True
    time = 0
    while load:
        time += 1
        screen.blit(loading_image, (0, 0))
        pyg.display.flip()
        if time >= 1000:
            load = False

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                raise SystemExit


# 定义开始界面
def starting_screen():     
    start = True
    play_button = Button('开始游戏', RED, None, 470, centered_x=True)  # 创建开始按钮
    instructions_button = Button('游戏说明', RED, None, 520, centered_x=True)  # 创建游戏说明按钮
    exit_button = Button('退出', RED, None, 590, centered_x=True)
    continue_game_button = Button('继续游戏', RED, None, 470, centered_x=True)  # 创建开始按钮
    again_button = Button('重新开始', RED, None, 470, centered_x=True)  # 创建开始按钮
    while start:
        global continue_game,t,remake
        screen.blit(start_ui, (0, 0))
        # play按键的颜色变化，鼠标移动到“play”时为红色，否则为黑色
        if continue_game == 'no':
            if play_button.check_click(pyg.mouse.get_pos()):
                play_button = Button('开始游戏', RED, None, 520, centered_x=True)
            else:
                play_button = Button('开始游戏', BLACK, None, 520, centered_x=True)
            play_button.display()
        elif continue_game == 'yes':
            if continue_game_button.check_click(pyg.mouse.get_pos()):
                continue_game_button = Button('继续游戏', RED, None, 480, centered_x=True)
            else:
                continue_game_button = Button('继续游戏', BLACK, None, 480, centered_x=True)
            
            if again_button.check_click(pyg.mouse.get_pos()):
                again_button = Button('重新开始', RED, None, 520, centered_x=True)
            else:
                again_button = Button('重新开始', BLACK, None, 520, centered_x=True)

            continue_game_button.display()
            again_button.display()

        # instructions按键的颜色变化，鼠标移动到“instructions”时为红色，否则为黑色
        if instructions_button.check_click(pyg.mouse.get_pos()):
            instructions_button = Button('游戏说明', RED, None, 560, centered_x=True)
        else:
            instructions_button = Button('游戏说明', BLACK, None, 560, centered_x=True)
        if exit_button.check_click(pyg.mouse.get_pos()):
            exit_button = Button('退出', RED, None, 600, centered_x=True)
        else:
            exit_button = Button('退出', BLACK, None, 600, centered_x=True)
        
        instructions_button.display()
        exit_button.display()
        pyg.display.flip()

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                raise SystemExit
        if pyg.mouse.get_pressed()[0]:
            if play_button.check_click(pyg.mouse.get_pos()):
                pyg.mixer.music.fadeout(1500)
                click_sound()
                start = False
                loading1() 
            if instructions_button.check_click(pyg.mouse.get_pos()):
                click_sound()
                explain_button()
            if again_button.check_click(pyg.mouse.get_pos()):
                click_sound()
                remake = 1
                start = False
            if continue_game_button.check_click(pyg.mouse.get_pos()):
                click_sound()
                start = False
            if exit_button.check_click(pyg.mouse.get_pos()):
                pyg.quit()
                raise SystemExit

#暂停界面
def stop():
    global run,all_stop
    stop = True
    again_button = Button('重玩', RED, None, 70, centered_x=True)  # 创建重新开始按钮
    exit_button = Button('退出', RED, None, 590, centered_x=True) #退出游戏按钮
    play_button = Button('退出', RED, None, 590, centered_x=True)  # 继续游戏按钮
    back_button = Button('退出', RED, None, 590, centered_x=True)  # 继续游戏按钮
    while stop:
        global remake,continue_game
        if again_button.check_click(pyg.mouse.get_pos()):
            again_button = Button('重新开始', RED,610, 380 - 200)
        else:
            again_button = Button('重新开始', BLACK,610, 380- 200)
        if exit_button.check_click(pyg.mouse.get_pos()):
            exit_button = Button('退出游戏', RED, 610, 430- 200)
        else:
            exit_button = Button('退出游戏', BLACK, 610, 430- 200)
        if play_button.check_click(pyg.mouse.get_pos()):
            play_button = Button('继续游戏', RED, 610, 330- 200)
        else:
            play_button = Button('继续游戏', BLACK, 610, 330- 200)
        if back_button.check_click(pyg.mouse.get_pos()):
            back_button = Button('返回主菜单', RED, 610, 480- 200)
        else:
            back_button = Button('返回主菜单', BLACK, 610, 480 - 200)

        screen.blit(hammer1, (boy_x - 100, boy_y - 120))
        sprite_list_fly.update()
        sprite_list_lady.update()
        sprite_list_lady_hit.update()
        screen.blit(stop_image, (325, 100- 100))
        play_button.display()
        again_button.display()
        exit_button.display()
        back_button.display()        
        pyg.display.update()

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                raise SystemExit
        if pyg.mouse.get_pressed()[0]:
            if play_button.check_click(pyg.mouse.get_pos()):
                click_sound()
                all_stop = 'no'
                stop = False
            if again_button.check_click(pyg.mouse.get_pos()):
                pyg.mixer.music.fadeout(1500)
                all_stop = 'no'
                click_sound()
                remake = 1
                stop = False
            if back_button.check_click(pyg.mouse.get_pos()):
                click_sound()
                continue_game = 'yes'
                all_stop = 'no'
                stop = False
                starting_screen()
            if exit_button.check_click(pyg.mouse.get_pos()):
                pyg.quit()
                raise SystemExit

font_addr = pyg.font.get_default_font()
font1 = pyg.font.Font('font/再见旧时光.ttf', 35)  # 按钮字体大小
starting_screen()

sprite_list_lady = pyg.sprite.Group()  # 瓢虫组
sprite_list_v = pyg.sprite.Group()  # 锤子、蔬菜组
sprite_list_fly = pyg.sprite.Group()  # 苍蝇组
sprite_list_lady_hit = pyg.sprite.Group()  # 瓢虫hit组
sprite_list_sss = pyg.sprite.Group() #全体害虫组
sprite_list_lazer = pyg.sprite.Group()  # 激光组
score_add_show_list = pyg.sprite.Group()  # 得分显示组
blue_list = pyg.sprite.Group()  # 蓝色粒子组
hammer_list = pyg.sprite.Group()

# 实例化蔬菜
vegetable1 = Vegetable(0, 70)
vegetable2 = Vegetable(0, 260)
vegetable3 = Vegetable(0, 460)

line = Line() #判定线

# 将蔬菜添加进锤子蔬菜组
sprite_list_v.add(vegetable1)
sprite_list_v.add(vegetable2)
sprite_list_v.add(vegetable3)

# 三个蔬菜的生命
live1 = 1
live2 = 1
live3 = 1

#(text, color, x, y, **kwargs)
stop_button = Button('返回', RED,30, 40)  # 暂停按钮
over_again_button = Button('重玩', RED, None, 350, centered_x=True)  # 创建重新开始按钮
over_return_button = Button('返回', RED, None, 400, centered_x=True)  # 创建游戏说明按钮
over_exit_button = Button('退出', RED, None, 450, centered_x=True)  # 创建退出按钮

remake = 1  # 重造开与关，开是1，关是0
over_show = 1  # 显示结束界面，1为开，0为关
last_score_remake = 1  # 重置上局游戏分数，1为开，0为关

#计数器
fffly = 0
lllady = 0

#计数器阈值
fffly_best = 2000 #用来定义的值，可以忽略
lllady_best = 2000

#all_stop
all_stop = 'no'

#害虫数量
number = 0 

#打到的害虫数量
hit_number = 0 

#能量
energy = 0
big_skill = 'no'
lazer1_move_y = 680
lazer2_move_y = 0
energy_text = pyg.font.Font('font/再见旧时光.ttf', 35)
energy_show1 = energy_text.render('能量', True, (0, 0, 0))
energy_show2 = energy_text.render('已充满!', True, (0, 0, 0))

def read_second():
    read = True
    three_x = -200
    two_x = -200
    one_x = -200
    black_x = -2000
    three_time = 0
    two_time = 0
    one_time = 0
    line1_y = -5
    line2_y = -5
    line3_y = -5
    line4_x = -5
    line5_x = 1371
    while read:
        
        screen.blit(backg, (0, 0))
        pyg.draw.line(screen, (0, 0, 0), (0, line1_y), (1366, line1_y), 5)#155
        pyg.draw.line(screen, (0, 0, 0), (0, line2_y), (1366, line2_y), 5) #155+195
        pyg.draw.line(screen,(0,0,0), (0,line3_y), (1366,line3_y), 5)#155+195+190
        pyg.draw.line(screen, (0, 0, 0), (line4_x, 0), (line4_x, 700), 5)  # 400
        screen.blit(boy, (180, 290))
        screen.blit(black_image, (black_x, 170))
        screen.blit(three, (three_x, 270))
        screen.blit(two, (two_x, 270))
        screen.blit(one, (one_x, 270))
        if line1_y < 155:
            line1_y += 5
        if line2_y < 155+195:
            line2_y += 5
        if line3_y < 155+195+190:
            line3_y += 5
        if line4_x < 400:
            line4_x += 5
        if line5_x > line4_x:
            pyg.draw.line(screen, (0, 0, 0), (line5_x, 0), (line5_x, 700), 5)  # 400
            line5_x -= 10
        
        if black_x < 0:
            black_x += 50
        if three_x < 600:
            three_x += 20
        if three_x == 600 and three_time < 50:
            three_time += 1
        if three_time >= 50 and three_x < 1450:
            three_x += 20
        if three_x >= 1450:
            if two_x < 600:
                two_x += 20
            if two_x == 600 and two_time < 50:
                two_time += 1
            if two_time >= 50 and two_x < 1450:
                two_x += 20
            if two_x >= 1460:
                if one_x < 600:
                    one_x += 20
                if one_x == 600 and one_time < 50:
                    one_time += 1
                if one_time >= 50:
                    one_x += 20
                    black_x += 45
                if one_x >= 1500:
                    fight_BGM()
                    read = False

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                raise SystemExit

        pyg.display.flip()
        pyg.time.delay(8)

# 正式进入游戏
while run:
    #能量
    if energy > 100:
        energy = 100
    if big_skill == 'yes':
        energy = 0
        lazer1 = Lazer1(lazer1_move_y)
        lazer2 = Lazer2(lazer2_move_y)
        sprite_list_lazer.add(lazer1)
        sprite_list_lazer.add(lazer2)
        lazer1_move_y -=50
        lazer2_move_y += 50
        if lazer2_move_y >= 2500:
            big_skill = 'no'
    if big_skill == 'no':
        lazer1_move_y = 680
        lazer2_move_y = 0

    fffly += 1
    lllady += 1
    if fffly >= fffly_best:
        fffly = 0
        fly = Fly(random.randint(1,15))
        sprite_list_fly.add(fly)
        sprite_list_sss.add(fly)
        number += 1

    
    if lllady >= lllady_best:
        lllady = 0
        ladybug = Ladybug(random.randint(1, 20))
        sprite_list_lady.add(ladybug)
        sprite_list_sss.add(ladybug)
        number += 1

    sprite_list_fly.update()
    sprite_list_lady.update()
    sprite_list_lady_hit.update()
    sprite_list_lazer.update()
    score_add_show_list.update()
    blue_list.update()
    hammer_list.update()

    #检测键盘
    keys_pressed = pyg.key.get_pressed()

    if last_score_remake == 1:
        last_score = score
        last_score_remake = 0  # 重置上局游戏分数，1为开，0为关

    if remake == 1:#重造程序        
        
        game_time = 0  # 游戏时间归零
        score = 0  # 分数归零
        live = 3  # 生命重置
        loss_score_change = 0
        energy = 0
        kill = 0  # 击杀数归零
        over_show = 1  # 启用结束界面
        # 让蔬菜回到原来的位置
        vegetable1.rect.y = 70
        vegetable2.rect.y = 260
        vegetable3.rect.y = 460

        # 让蔬菜重新活
        live1 = 1
        live2 = 1
        live3 = 1

        fffly = 0

        lllady = 0
        read_second()
        boy_y = 290

        remake = 0  # 关闭重造程序
    
    #暂停键
    stop_button.display()
    if stop_button.check_click(pyg.mouse.get_pos()):
        stop_button = Button('暂停', RED,1260,10)
    else:
        stop_button = Button('暂停', BLACK, 1260, 10)

    Score(score)
    pyg.display.flip()
    pyg.time.delay(8)
    screen.blit(backg, (0, 0))  # 显示背景
    pyg.draw.line(screen, (0, 0, 0), (0, 155), (1366, 155), 5)
    pyg.draw.line(screen, (0, 0, 0), (0, 155+195), (1366, 155+195), 5)
    pyg.draw.line(screen,(0,0,0), (0,155+195+190), (1366,155+195+190), 5)
    pyg.draw.line(screen, (0, 0, 0), (400, 0), (400, 700), 5)
    if live > 0:
        screen.blit(image_energy, (560, 620))
        if energy < 100:
            pyg.draw.line(screen, RED, (661, 626), (661, 673), int(energy*1.94))
            screen.blit(energy_show1, (630, 630))
        if energy >= 100:
            pyg.draw.line(screen,(255, 0, random.randint(1, 255)), (661, 626), (661, 673), int(energy*1.94))
            screen.blit(energy_show2, (610, 630))
    if big_skill == 'no':
        screen.blit(boy, (boy_x, boy_y))  # 显示人物
    if big_skill == 'yes':
        screen.blit(angry_boy, (boy_x, boy_y))  # 显示人物
    game_time += 1

    # 蔬菜精灵与害虫精灵组的碰撞
    collide_sprite_v1 = pyg.sprite.spritecollide(vegetable1,sprite_list_sss,False)
    if collide_sprite_v1:
        eat_sound()
        live -= 1
        live1 = 0
        vegetable1.rect.y = 1000  # 让蔬菜消失

    collide_sprite_v2 = pyg.sprite.spritecollide(vegetable2,sprite_list_sss,False)
    if collide_sprite_v2:
        eat_sound()
        live -= 1
        live2 = 0
        vegetable2.rect.y = 1000

    collide_sprite_v3 = pyg.sprite.spritecollide(vegetable3,sprite_list_sss,False)
    if collide_sprite_v3:
        eat_sound()
        live -= 1
        live3 = 0
        vegetable3.rect.y = 1000

    # 如果蔬菜没有被害虫碰到
    if live1 == 1:
        vegetable1.spawn_stay()
    if live2 == 1:
        vegetable2.spawn_stay()
    if live3 == 1:
        vegetable3.spawn_stay()

    collide_sprite_v4 = pyg.sprite.spritecollide(line,sprite_list_sss,True)# 如果害虫过了线就减分
    if collide_sprite_v4:
        energy -= 1

    # 检测事件，用于检测是否按了右上角退出按钮和z,x,c,空格键
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            raise SystemExit
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_z:
                boy_y = 100
            elif event.key == pyg.K_x:
                boy_y = 290
            elif event.key == pyg.K_c:
                boy_y = 480
            elif event.key == pyg.K_v:
                if energy >= 100:
                    lazer_sound.set_volume(0.5)
                    lazer_sound.play()
                    energy = 0
                    big_skill = 'yes'

            elif event.key == pyg.K_SPACE:
                attack_sound()#播放锤子击打的声音
                hammer=Hammer(boy_x + 190, boy_y+30)  # 创建锤子
                hammer_list.add(hammer)


        # 游戏内的按钮
        elif pyg.mouse.get_pressed()[0]:
            if stop_button.check_click(pyg.mouse.get_pos()):
                all_stop = 'yes'
                stop()
                click_sound()
                        
    #锤子
    if keys_pressed[pyg.K_SPACE]:
        heat = 1#切换锤子形态
        screen.blit(hammer0,(boy_x + 70, boy_y))
    else:
        heat = 0 #让锤子回到标准状态
    if game_time > 0 and heat == 0:
        screen.blit(hammer1, (boy_x - 105, boy_y - 120))

    # 刷怪机制，跟游戏时间game_time有关，游戏时间越大游戏难度越难
    if 0 < game_time <= 2500:
        fffly_best = 100
        lllady_best = 250
    if 2500 < game_time <= 4000:
        fffly_best = 100
        lllady_best = 250
    if 4000 < game_time <= 5000:
        fffly_best = 50
        lllady_best = 230
    if game_time > 5000:
        fffly_best = 20
        lllady_best = 200
    if 0 < game_time <= 35 and loss_score_change == 0:
        loss_score = -15
        loss_score_change = 1
    if 35 < game_time <= 60 and loss_score_change == 1:
        loss_score = -50
        loss_score_change = 2
    if 60 < game_time <= 90 and loss_score_change == 2:
        loss_score = -150
        loss_score_change = 3
    if 90 < game_time <= 200 and loss_score_change == 3:
        loss_score = -200
        loss_score_change = 4
    if 200 < game_time <= 400 and loss_score_change == 4:
        loss_score = -300
        loss_score_change = 5
    if 400 < game_time and loss_score_change == 5:
        loss_score = -500
        loss_score_change = 0
    if live == 0 and remake == 0:  # 如果你死了
        if 20000 <= score:
            rank = 'SSS'
        elif 16000 <= score < 20000:
            rank = 'SS'
        elif 13000 <= score < 16000:
            rank = 'S'
        elif 10000 <= score < 12000:
            rank = 'A'
        elif 6000 <= score < 10000:
            rank = 'B'
        elif 1500 <= score < 6000:
            rank = 'C'
        elif 100 <= score < 1500:
            rank = 'D'
        elif -500 <= score < 100:
            rank = 'E'
        elif score < -500:
            rank = 'F'
        if score > last_score:
            best_score = score
        best_score_txt = open('data/best_score.txt', 'w')
        best_score_txt.write(str(best_score))
        best_score_txt.close()
        game_over1()
        #这是最后一个版本，估计以后不会更新了


    
