import pygame
import math
from sys import exit
pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("projectile test")
ball_xpos = 0
ball_ypos = 190
line_y = ball_ypos + 30
ball_rect = pygame.Rect(ball_xpos, ball_ypos, 30, 30)
angle = 0
velocity = 0
final = 0
initial = 0
result = final - initial
distance = result
text_surface = pygame.font.Font(None, 30)
velx, vely = 0, 0 # we can affect the angle this way
fps = pygame.time.Clock()
clicked = False
draw_line = False
released = False
grounded = True
while True:
    mouse_pos = pygame.mouse.get_pos()
    # store the mouse component in a new variable
    mx, my = mouse_pos
    # x component of the projectile
    xvel = (mx - ball_rect.x -15) // 10
    # y component of the projectile
    yvel = (ball_rect.y - my + 15) // 10
    text1 = text_surface.render(f"angle: {angle}", True, "blue")
    text2 = text_surface.render(f"velocity: {velocity}",True, "green")   
    text3 = text_surface.render(f"distance: {distance}m",True, "Red")   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # sets clicked variable to true if mouse is pressed and mouse is touching ball
        if event.type == pygame.MOUSEBUTTONDOWN and ball_rect.collidepoint(mouse_pos) and grounded:
            clicked = True
            initial = ball_rect.x
        if event.type == pygame.MOUSEBUTTONUP and ball_rect.collidepoint(mouse_pos) == False:
            draw_line = False
            clicked = False
            released = True
        if clicked:
            draw_line = True
        if grounded and clicked:
            velx = xvel
            vely = yvel
    screen.fill("black")
    screen.blit(text1,(5, 5))
    screen.blit(text2, (5,30))
    screen.blit(text3, (5,55))
    pygame.draw.ellipse(screen, "green", ball_rect, 3)
    pygame.draw.line(screen, "blue", (0, line_y), (500,line_y))
    if draw_line:
        pygame.draw.line(screen, "white", (ball_rect.x+15, ball_rect.y+15), mouse_pos ,3)
        print(xvel, yvel)
        velocity = int(math.sqrt(yvel*yvel + xvel*xvel))
        angle = int(math.degrees(math.atan2(yvel, xvel)))
    # shoot the ball when it is released
    if released:
        grounded = False
        ball_rect.x += velx
        ball_rect.y -= vely
        #for the projectile to travel a parabolic path accelaration must happen in the y axis only
        vely -= 0.49
    print(xvel, yvel)
    # stop movement in the x direction if the ball is on the ground
    if ball_rect.bottom -3 >= line_y:
        ball_rect.bottom = line_y
        velx = 0
        grounded = True
        released = False
        final = ball_rect.x
        distance = abs(final - initial)
    fps.tick(20)
    pygame.display.update()
