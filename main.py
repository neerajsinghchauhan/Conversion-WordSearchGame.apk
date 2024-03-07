import os
import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.lang import Builder

# Determine the path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load images
background_image = os.path.join(current_dir, 'WordSearch-Game.png')
splash_image = os.path.join(current_dir, 'WordSearch-Gamesplash.png')

# Grids for different levels
grids = {
    'easy': (5, 5),
    'medium': (8, 8),
    'hard': (10, 10),
    'expert': (12, 12),
    'master': (15, 15),
    'legendary': (18, 18),
    'godlike': (20, 20),
    'unbeatable': (22, 22),
    'impossible': (25, 25),
    'insane': (30, 30)
}

# Word lists for different levels
words = {
    'easy': ['PYTHON', 'KIVY', 'WORD', 'SEARCH', 'GAME'],
    'medium': ['DEVELOPMENT', 'CHALLENGE', 'PUZZLE', 'PROGRAMMING', 'FUN'],
    'hard': ['AI', 'OPENAI', 'PYTHONISTA', 'PYTHONIC', 'ALGORITHM'],
    'expert': ['COMPUTER', 'SCIENCE', 'CODING', 'ENGINEER', 'INTELLIGENCE'],
    'master': ['LEARNING', 'DATA', 'ANALYSIS', 'RESEARCH', 'PROJECT'],
    'legendary': ['EXPERIMENT', 'INNOVATION', 'TECHNOLOGY', 'SOFTWARE', 'HARDWARE'],
    'godlike': ['DEVELOPER', 'WEB', 'APPLICATION', 'MOBILE', 'INTERFACE'],
    'unbeatable': ['USER', 'EXPERIENCE', 'DESIGN', 'ITERATION', 'ITERATIVE'],
    'impossible': ['PROCESS', 'SOLUTION', 'PROBLEM', 'ALGORITHM', 'EFFICIENT'],
    'insane': ['DATA', 'STRUCTURE', 'ABSTRACTION', 'PARADIGM', 'PYTHONISTA']
}

Builder.load_file('word_search.kv')

class WordSearchApp(App):
    def build(self):
        return LevelSelection()

if __name__ == "__main__":
    WordSearchApp().run()
