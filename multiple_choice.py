import pygame, sys
import random
import tkinter
from pygame.locals import *
from tkinter import filedialog
import re


file_path = "students.txt"
temp_names = []

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE  = (36, 138, 212)
RED   = (229, 90, 34)
GREEN = (28, 235, 40)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Name Picker")

# pick a font you have and set its size
myfont = pygame.font.SysFont("arial", 50)


DISPLAYSURF.fill(BLUE)
pygame.display.update()

#---------------------------
# Open a file and import text information and create data-maps

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

file_path= filedialog.askopenfilename()

names_file = open(file_path, "r")
lines = names_file.readlines()


'''
Aiken Format
What is the correct answer to this question?
A. Is it this one?
B. Maybe this answer?
C. Possibly this one?
D. Must be this one!
ANSWER: D
'''


"""
master_dict = { '8A': {'noah_8a': [0,0,0,0],'chris_8a': [0,0,0,0]},
                '7A': {'greg_7a': [0,0,0,0],'kate_7a': [0,0,0,0]}
                }
"""

quiz_content = ""

current_key = ""
for line in lines:

    
    quiz_content = quiz_content + line
   
names_file.close()

#split_line = quiz_content.split('ANSWER: |/n/n')

split_line = re.split('ANSWER: |\n\n',quiz_content)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
   



count = 0  

# Beginning Game Loop
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
            
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                count = count + 1
                
            if event.key == K_LEFT:
                count = count - 1

                
    # print selected name
    DISPLAYSURF.fill(BLUE)        
    
    '''
    label = myfont.render(split_line[count], 1, BLACK)
    text_rect = label.get_rect(center=(800/2, 800/2))
    DISPLAYSURF.blit(label, text_rect)
    '''
    
    blit_text(DISPLAYSURF, split_line[count], (20, 20), myfont)


   
    # response modification
    pygame.display.update()
    
    FramePerSec.tick(FPS)
    
