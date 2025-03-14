import pygame
import random


class Level:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Level 4: Catch the Falling Objects")
        self.clock = pygame.time.Clock()
        self.running = True
        self.completed = False

        # Player properties
        self.player = pygame.Rect(self.width // 2 - 25, self.height - 50, 50, 10)
        self.player_speed = 5

        # Falling objects properties
        self.objects = []
        self.object_speed = 3
        self.spawn_timer = 0
        self.catch_goal = 5  # Need to catch 5 to complete
        self.caught = 0

    def spawn_object(self):
        x_pos = random.randint(20, self.width - 20)
        self.objects.append(pygame.Rect(x_pos, 0, 20, 20))

    def move_objects(self):
        for obj in self.objects[:]:
            obj.y += self.object_speed
            if obj.y > self.height:
                self.objects.remove(obj)
            elif self.player.colliderect(obj):
                self.objects.remove(obj)
                self.caught += 1
                if self.caught >= self.catch_goal:
                    self.completed = True
                    self.running = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player.x > 0:
            self.player.x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player.x < self.width - self.player.width:
            self.player.x += self.player_speed

    def draw_game(self):
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, (0, 255, 0), self.player)
        for obj in self.objects:
            pygame.draw.rect(self.screen, (255, 0, 0), obj)
        pygame.display.flip()

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            self.handle_input()
            self.move_objects()

            if self.spawn_timer == 0 or self.spawn_timer > 30:
                self.spawn_object()
                self.spawn_timer = 0
            self.spawn_timer += 1

            self.draw_game()
            self.clock.tick(30)

        pygame.quit()
        return self.completed