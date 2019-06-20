from tkinter import *
from time import *
import random



#################
#### ФУНКЦИИ ####
#################

def draw_pacman():
    canvas.create_image(x, y, image=eater)
    canvas.create_text(70, 30, text=f"SCORE: {str(points)}", font="Impact 24 bold", fill='#ffffff')


def draw_food():
    canvas.create_image(0, 0, image=bg_img, anchor=NW)
    global x_food, y_food
    canvas.create_image(x_food, y_food, image=food)


def draw_update():
    canvas.delete('all')
    draw_food()
    draw_pacman()
    canvas.update()


def movement_down(event):  # вижение вниз
    if points != win:
        global x, y
        if y < 570:
            y = y + 10
        draw_update()


def movement_up(event):  # движение вверх
    if points != win:
        global x, y
        if y > 30:
            y = y - 10
        draw_update()


def movement_right(event):  # движение вправо
    if points != win:
        global x, y
        if x < 775:
            x = x + 10
        draw_update()


def movement_left(event):  # даижение влево
    if points != win:
        global x, y
        if x > 30:
            x = x - 10
        draw_update()


###########################
#### КОНФИГУРАЦИЯ ОКНА ####
###########################

root = Tk()
root.iconbitmap('./assets/favicon.ico')
canvas = Canvas(width=800, height=600, bg='#23272A')  # размер окна
canvas.pack()
root.title("bruh")  # лучший аниме тайтл
root.resizable(False, False)  # делаем тайтл не ресайзбл

##############################
#### ПОДКЛЮЧЕНИЕ КАРТИНОК ####
##############################

eater = PhotoImage(file="./assets/eater.png")  # stevie
food = PhotoImage(file="./assets/food.png")  # apples
# win_img = Image.open(file="win_img.jpg")
bg_img = PhotoImage(file="./assets/bg.png")

###################
#### ОТРИСОВКА ####
###################

x = 200
y = 200

x_food = random.randint(64, 768)
y_food = random.randint(64, 568)

points = 0
win = 25

################
#### CHEAT #####
################

def cheat_win(event):
    global points
    points = 999999999999999999999


root.bind(["e", "z", "<w>", "<i>", "<n>"], func=cheat_win)

root.bind("<Down>", func=movement_down)  # слушатель нажатий
root.bind("<s>", func=movement_down)
root.bind("<Up>", func=movement_up)
root.bind("<w>", func=movement_up)
root.bind("<Right>", func=movement_right)
root.bind("<d>", func=movement_right)
root.bind("<Left>", func=movement_left)
root.bind("<a>", func=movement_left)

draw_pacman()

while points < win:
    if x+32 > x_food and x+32 < x_food + 64 and y > y_food and y < y_food + 64:
        x_food, y_food = random.randint(64, 768), random.randint(64, 568)
        points += 1
    draw_update()
    print(points)

canvas.delete('all')

canvas.create_image(0, 0, image=bg_img, anchor=NW)

canvas.create_text(350, 250, \
                   text="            CONGRATULATIONS!\n        YOU HEALED YOURSELF!", fill="white", \
                   font="Impact 32 bold")
canvas.create_text(720, 570, font="Arial 12", text=" Made by Defracted\ngithub: @runic-tears",fill="white")

root.mainloop()