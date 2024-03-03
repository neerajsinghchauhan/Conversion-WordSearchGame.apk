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

class HintPopup(Popup):
    def __init__(self, hint_text, **kwargs):
        super(HintPopup, self).__init__(**kwargs)
        self.title = 'Hint'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        hint_label = Label(text=hint_text, size_hint=(1, 0.8))
        close_button = Button(text='Close', size_hint=(1, 0.2))
        close_button.bind(on_release=self.dismiss)
        
        self.content = BoxLayout(orientation='vertical')
        self.content.add_widget(hint_label)
        self.content.add_widget(close_button)

class LevelSelection(BoxLayout):
    def __init__(self, **kwargs):
        super(LevelSelection, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.levels = ['easy', 'medium', 'hard']
        for level in self.levels:
            button = Button(text=level.capitalize(), size_hint=(1, None), height=50)
            button.bind(on_release=lambda instance, level=level: self.start_game(level))
            hint_button = Button(text='Hint', size_hint=(1, None), height=50)
            hint_button.bind(on_release=lambda instance, level=level: self.show_hint(level))
            self.add_widget(button)
            self.add_widget(hint_button)
            
    def start_game(self, level):
        game_screen = WordSearchGame(level=level)
        self.parent.add_widget(game_screen)
        self.parent.remove_widget(self)
        
    def show_hint(self, level):
        hint_text = "This is a hint for level: {}".format(level)
        hint_popup = HintPopup(hint_text)
        hint_popup.open()

class WordSearchGame(GridLayout):
    time = NumericProperty(60)  # Timer starts at 60 seconds
    score = NumericProperty(0)
    level = StringProperty('easy')
    stars = NumericProperty(0)

    def __init__(self, **kwargs):
        super(WordSearchGame, self).__init__(**kwargs)
        self.cols, self.rows = grids[self.level]
        self.grid = self.generate_grid(self.level)
        self.selected_letters = []
        self.selected_word = ''
        self.found_words = set()
        self.populate_grid()
        Clock.schedule_interval(self.update_timer, 1)

    def generate_grid(self, level):
        return [[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(self.cols)] for _ in range(self.rows)]

    def populate_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                button = Button(text=self.grid[row][col])
                button.row = row
                button.col = col
                button.bind(on_press=self.select_letter)
                self.add_widget(button)

    def select_letter(self, instance):
        row, col = instance.row, instance.col
        self.selected_letters.append((row, col))
        self.selected_word += self.grid[row][col]
        instance.disabled = True
        Clock.schedule_once(self.check_word, 0.5)

    def check_word(self, dt):
        if self.selected_word in words[self.level] and self.selected_word not in self.found_words:
            self.score += len(self.selected_word)
            self.found_words.add(self.selected_word)
            for row, col in self.selected_letters:
                self.children[row * self.cols + col].background_color = (0, 1, 0, 1)
        else:
            for row, col in self.selected_letters:
                self.children[row * self.cols + col].disabled = False
        self.selected_letters = []
        self.selected_word = ''

        if len(self.found_words) == len(words[self.level]):
            self.stars += 1

    def update_timer(self, dt):
        self.time -= 1
        if self.time <= 0:
            Clock.unschedule(self.update_timer)
            self.end_game()

    def end_game(self):
        # Perform end game actions
        pass

class WordSearchApp(App):
    def build(self):
        return LevelSelection()

if __name__ == "__main__":
    WordSearchApp().run()
