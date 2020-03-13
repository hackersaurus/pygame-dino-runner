import pygame

GAME_TITLE = "T-Rex Runner"
MAX_WIDTH = 500
MAX_HEIGHT = 500
DELAY_MS = 10


class GameObject:
    
    def __init__(self, position=(0, 0), size=(50, 50), color=(0, 0, 0)):
        self._x_pos, self._y_pos = position
        self._width, self._height = size
        self._color = color
    
    def draw(self, window):
        location = (self._x_pos, self._y_pos, self._width, self._height)
        pygame.draw.rect(window, self._color, location)
        

if __name__ == '__main__':
    
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    
    player = GameObject(color=(0, 130, 130))
    
    vel = 5
    
    run_game = True
    while run_game: 
        pygame.time.delay(DELAY_MS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            player._x_pos -= vel
        if keys[pygame.K_RIGHT]:
            player._x_pos += vel
        if keys[pygame.K_UP]:
            player._y_pos -= vel
        if keys[pygame.K_DOWN]:
            player._y_pos += vel
                
        window.fill((0, 0, 0))
        player.draw(window)
        pygame.display.update()
    
    pygame.quit()