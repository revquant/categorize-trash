import pgzrun
#import pygame
from random import randint, choice
#pygame.mixer.init()
#pygame.mixer.music.load("/Users/revquant/Downloads/hackathon_stuff/Water.mp3")
#pygame.mixer.music.play(1, 1)
points = 0
won = None
skip = Actor('skip')
cardboard = Actor('cardboard')
bananapeel = Actor('bananapeel')
ceramics = Actor('ceramics')
coffee = Actor('coffeegrounds')
cornhusk = Actor('cornhusk')
leaves = Actor('deadleaves')
glass = Actor('glass')
bulb = Actor('lightbulb')
mirror = Actor('mirror')
orange = Actor('orangepeel')
paper = Actor('paper')
plastic = Actor('plasticbottle')
soda = Actor('soda')
stalebread = Actor('stalebread')
styrofoam = Actor('styrofoam')
teabag = Actor('teabag')
recyclebin = Actor('recyclebin')
trashbin = Actor('trashbin')
compostbin = Actor('compostbin')
trash = [ceramics, mirror, styrofoam, bulb]
recycle = [cardboard, soda, glass, paper, plastic]
compost = [bananapeel, coffee, cornhusk, leaves, orange, stalebread, teabag]
def pick_item():
    which = randint(1, 3)
    if which == 1:
        category = trash
    elif which == 2:
        category = recycle
    else:
        category = compost
    item = choice(category)
    return item
def is_in_category(item, category):
    if item in category:
        return True
    else:
        return False
def on_mouse_down(pos):
    global points, won
    if recyclebin.collidepoint(pos):
        if is_in_category(item, recycle):
            points += 1
        else:
            points -= 1
    elif trashbin.collidepoint(pos):
        if is_in_category(item, trash):
            points += 1
        else:
            points -= 1
    elif compostbin.collidepoint(pos):
        if is_in_category(item, compost):
            points += 1
        else:
            points -= 1
    elif skip.collidepoint(pos):
        points -= 0.5
    if points >= 20:
        won = True
    elif points <= -20:
        won = False
    draw()

def draw():
    global item, category, trash, recycle, compost, won, recyclebin, compostbin
    screen.clear()
    screen.draw.text('Points: ' + str(points), topright=(700, 50), color="skyblue", fontsize=32)
    item = pick_item()
    item.pos = 400, 150
    item.draw()
    if is_in_category(item, trash):
        category = trash
    elif is_in_category(item, recycle):
        category = recycle
    else:
        category = compost
    recyclebin.pos = 700, 450
    recyclebin.draw()
    trashbin.pos = 400, 450
    trashbin.draw()
    compostbin.pos = 125, 450
    compostbin.draw()
    skip.pos = 125, 90
    skip.draw()
    if won == True:
        screen.clear()
        screen.draw.text('You won!', topleft=(375, 250), color="skyblue", fontsize=32)
    elif won == False:
        screen.clear()
        screen.draw.text('You lost!', topleft=(375, 250), color="skyblue", fontsize=32)
pgzrun.go()