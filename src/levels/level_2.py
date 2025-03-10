from asciimatics.screen import Screen


class Level:
    def __init__(self):
        self.player_x = 1
        self.player_y = 1
        self.completed = False  # Track level completion
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
        for y, row in enumerate(self.maze):
            screen.print_at(row, 0, y)
        screen.print_at("P", self.player_x, self.player_y, colour=2)
        screen.refresh()

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
            self.draw_maze(screen)
            event = screen.get_key()

            if event in (ord('q'), ord('Q')):
                break  # Quit game

            if event == Screen.KEY_UP:
                self.move(0, -1)
            elif event == Screen.KEY_DOWN:
                self.move(0, 1)
            elif event == Screen.KEY_LEFT:
                self.move(-1, 0)
            elif event == Screen.KEY_RIGHT:
                self.move(1, 0)

        return self.completed  # Return True if level is completed

    def start(self):
        return Screen.wrapper(self.game_loop)