import os
from asciimatics.screen import Screen

os.environ['TERM'] = 'xterm-256color'

class Level:
    def __init__(self):
        self.player_x = 1
        self.player_y = 1
        self.completed = False  # Track level completion
        self.exit_x = 18
        self.exit_y = 9
        self.maze = [
            "####################",
            "#P       #        #",
            "# ####### # #######",
            "#       #   #     #",
            "####### ##### #####",
            "#     #       #   #",
            "# ### ####### ### #",
            "#   #       #     #",
            "##### ### ####### #",
            "#       #        E#",
            "####################"
        ]

    def draw_maze(self, screen):
        screen.clear()  # Clear the screen before drawing
        for y, row in enumerate(self.maze):
            screen.print_at(row[:20], 0, y)  # Ensure row is 20 characters wide
        screen.print_at("P", self.player_x, self.player_y, colour=2)
        screen.refresh()  # Refresh the screen to apply changes

    def move(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy

        if self.maze[new_y][new_x] == "#":
            return  # Blocked by wall

        self.player_x = new_x
        self.player_y = new_y

        if self.maze[new_y][new_x] == "E":
            self.completed = True  # Mark level as completed

    def game_loop(self, screen):
        while not self.completed:
            event = screen.get_event()
            if event is not None:
                if event == Screen.KEY_UP:
                    self.move_player(0, -1)
                elif event == Screen.KEY_DOWN:
                    self.move_player(0, 1)
                elif event == Screen.KEY_LEFT:
                    self.move_player(-1, 0)
                elif event == Screen.KEY_RIGHT:
                    self.move_player(1, 0)

            self.draw_maze(screen)
            screen.refresh()

            if self.check_completion():
                self.completed = True

    def move_player(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        if self.is_valid_move(new_x, new_y):
            self.player_x = new_x
            self.player_y = new_y

    def is_valid_move(self, x, y):
        # Check if the move is within bounds and not a wall
        return 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze) and self.maze[y][x] != "#"

    def check_completion(self):
        # Check if the player has reached the exit
        return self.player_x == self.exit_x and self.player_y == self.exit_y

    def start(self):
        return Screen.wrapper(self.game_loop)