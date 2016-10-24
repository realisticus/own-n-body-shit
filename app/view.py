import time
import tkinter as tk
import sys

from utils import *

class GravitationalSystemDrawer:
    '''This is the module, which directly draws the gravitational system. 
    It is based on a tkinter module.'''

    __DEFAULT_ANIMATION_DELAY = 0.025
    __PAUSE = False
    __EXIT = False
    #__SHOW_FORCE_LINES = False


    def __init__(self, gravitational_system, window_width, window_height, canvas_color):


        self.root = tk.TK()
        self.root.resizable(0,0)
        self.canvas = Canvas(self.root, width=window_width, 
        					 height=window_height, bg=canvas_color)
        
        self.gravitational_system = gravitational_system
        self.screen_elements = []

        self.__update_elements()

        self.canvas.pack()

        #add binds (force lines, pause, exit, and easter_egg for Gro)
        



