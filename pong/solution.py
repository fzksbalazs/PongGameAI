import pygame
pygame.init()



WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (225,225,225)
GREEN = (0,128,0)
BLACK = (0,0,0)

PADDLE_WIDTH , PADDLE_HEIGHT = 20,100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("Oswald ExtraLight", 50)
WINNING_SCORE = 5

class Ball:
    MAX_VEL = 5
    COLOR = WHITE
    
    def __init__(self, x, y, radius):
        self.x = self.original_x =  x
        self.y = self.original_y =  y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR,(self.x, self.y), self.radius)
        
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


class Paddle:
    COLOR = WHITE
    VEL = 4
    
    def __init__(self, x,y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y =  y
        self.width = width
        self.height = height
        
        
    def draw (self,win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
        
    def move (self, up=True):
        if up:
            self.y -= self.VEL    
        else:
            self.y += self.VEL   
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        
        
def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)
    
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) -
                                right_score_text.get_width()//2, 20))
    
    for paddle in paddles:
        paddle.draw(win)
        
        
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))
    
    ball.draw(win)
    pygame.display.update()
    

   
   


def main():
    run = True
    clock = pygame.time.Clock()
    
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT )
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH , HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT )
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS )
    
    left_score = 0
    right_score = 0
    
    
    
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)
        
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            ball.reset()
            left_score += 1
            
        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Bal oldali játékos nyert!"
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Jobb oldali játékos nyert!"

        if won:
            text = SCORE_FONT.render(win_text, 1, GREEN)
            WIN.blit(text, (WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0
        
    pygame.quit()
    
if __name__ == '__main__':
    main()