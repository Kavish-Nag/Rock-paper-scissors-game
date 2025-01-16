import pygame 
import random

pygame.init()
buttonc = (200, 200, 200)
ch = ["Rock", "Paper", "Scissors"]

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Rock Paper Scissors")
font = pygame.font.Font(None, 36)

def text(text, x, y):
    text = font.render(text,True,(0, 0, 0))
    screen.blit(text, (x, y))

def main():
    player = ""
    computer = ""
    result = ""
    rockb = pygame.Rect(50, 100, 200, 50)
    paperb = pygame.Rect(50, 170, 200, 50)
    scissorsb = pygame.Rect(50, 240, 200, 50)

    while True:
        screen.fill((0, 255, 255))
        pygame.draw.rect(screen, buttonc, rockb)
        pygame.draw.rect(screen, buttonc, paperb)
        pygame.draw.rect(screen, buttonc, scissorsb)
        
        text("Rock", 100, 110)
        text("Paper", 100, 180)
        text("Scissors", 100, 250)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos() 

                if rockb.collidepoint(mouse):
                    player = "Rock"
                elif paperb.collidepoint(mouse):
                    player = "Paper"
                elif scissorsb.collidepoint(mouse):
                    player = "Scissors"
                
                if player:
                    computer = random.choice(ch)
                    if player == computer:
                        result = "It's a tie!"
                    elif (player == "Rock" and computer == "Scissors") or \
                         (player == "Paper" and computer == "Rock") or \
                         (player == "Scissors" and computer == "Paper"):
                        result = "You win!"
                    else:
                        result = "You lose!"

        if player:
            text(f"Your choice: {player}", 300, 100)
            text(f"Computer's choice: {computer}", 300, 150)
            text(result, 300, 200)
        
        pygame.display.update()

main()
