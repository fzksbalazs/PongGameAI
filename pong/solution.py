import pygame
from Class import Game

class PongGame:
    def __init__(self, window, width, height) :
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_padddle = self.game.right_paddle
        self.ball = self.game.ball
        
    def test_ai(self):
        run =  True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                game.move_paddle(left=True, up=True)
            if keys[pygame.K_s]:
                game.move_paddle(left=True, up=False)
            
            game.loop()
            game.draw()
            pygame.display.update()
    
        pygame.quit()
        
        


width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)


