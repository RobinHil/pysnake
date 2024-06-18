import tkinter as tk
import random
import os

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()
        
        self.is_running = False
        self.game_over = False
        self.high_score = self.load_high_score()
        self.create_welcome_screen()
        
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def get_center_coords(self):
        return self.canvas_width // 2, self.canvas_height // 2
        
    def create_welcome_screen(self):
        self.canvas.delete(tk.ALL)
        center_x, center_y = self.get_center_coords()
        self.canvas.create_text(center_x, center_y - 50, text="Welcome to Snake Game", fill="white", font=("Arial", 24), tag="welcome")
        self.canvas.create_text(center_x, center_y, text="Press SPACE to start", fill="white", font=("Arial", 18), tag="welcome")
        self.canvas.create_text(center_x, center_y + 50, text=f"High Score: {self.high_score}", fill="white", font=("Arial", 18), tag="welcome")
        
    def create_game_over_screen(self):
        self.canvas.delete("score")
        center_x, center_y = self.get_center_coords()
        self.canvas.create_text(center_x, center_y - 50, text="Game Over", fill="white", font=("Arial", 24), tag="gameover")
        self.canvas.create_text(center_x - 100, center_y, text=f"Your Score: {self.score}", fill="white", font=("Arial", 18), tag="gameover")
        self.canvas.create_text(center_x + 100, center_y, text=f"High Score: {self.high_score}", fill="white", font=("Arial", 18), tag="gameover")
        self.canvas.create_text(center_x, center_y + 50, text="Press SPACE to restart", fill="white", font=("Arial", 18), tag="gameover")
        
    def init_game(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_direction = "Right"
        self.food_position = self.set_new_food_position()
        self.score = 0
        self.game_over = False
        self.create_objects()
        
    def create_objects(self):
        self.canvas.delete("all")
        if self.is_running:
            self.score_text = self.canvas.create_text(50, 25, text=f"Score: {self.score}", fill="white", font=("Arial", 16), tag="score")
        self.create_snake()
        self.create_food()
        
    def create_snake(self):
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tag="snake")
            
    def create_food(self):
        x, y = self.food_position
        self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red", tag="food")
        
    def set_new_food_position(self):
        while True:
            x = random.randint(0, 59) * 10
            y = random.randint(0, 39) * 10
            food_position = (x, y)
            if food_position not in self.snake:
                return food_position
        
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.snake_direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.snake_direction == "Down":
            new_head = (head_x, head_y + 10)
        elif self.snake_direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.snake_direction == "Right":
            new_head = (head_x + 10, head_y)
            
        self.snake = [new_head] + self.snake
        
        if self.snake[0] == self.food_position:
            self.food_position = self.set_new_food_position()
            self.score += 1
            self.canvas.itemconfigure(self.score_text, text=f"Score: {self.score}")
        else:
            self.snake.pop()
            
    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if not (0 <= head_x < 600 and 0 <= head_y < 400):
            return True
        if len(self.snake) != len(set(self.snake)):
            return True
        return False
        
    def on_key_press(self, e):
        new_direction = e.keysym
        if self.game_over and new_direction == "space":
            self.is_running = True
            self.init_game()
            self.run_game()
        elif not self.is_running and new_direction == "space":
            self.is_running = True
            self.init_game()
            self.run_game()
        else:
            all_directions = {"Up", "Down", "Left", "Right"}
            opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            
            if new_direction in all_directions and new_direction != opposites[self.snake_direction]:
                self.snake_direction = new_direction
            
    def run_game(self):
        if self.check_collisions():
            if self.score > self.high_score:
                self.high_score = self.score
            self.create_game_over_screen()
            self.game_over = True
            self.is_running = False
            return
        
        self.move_snake()
        self.create_objects()
        self.root.after(100, self.run_game)

    def load_high_score(self):
        if os.path.exists(".high_score"):
            with open(".high_score", "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self):
        with open(".high_score", "w") as file:
            file.write(str(self.high_score))
    
    def on_closing(self):
        self.save_high_score()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
