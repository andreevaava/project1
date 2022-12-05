import pygame
from random import randint

FPS = 60
WW=700
WH=500
#фон
BLACK = (15, 0, 0)
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 255, 127)
YELLOW = (255, 255, 0)
PINK = (235, 108, 163)
YELLOW2 = (238, 247, 107)
CORAL = (255, 127, 80)
radius = 40
#массив с вопросами
zadanie = [
'сколько костей в языке?',
'на стадии эмбриона у человека ... пар жабр?',
'сколько дней живет муха?',
'сколько микротрубочек в триплете?',
'сколько стадий в митозе?',
'сколько царств по Уиттекеру',
'кол-во ходильных конечностей у насекомых?',
'pH нейтральной среды',
'сколько ходильных конечностей у пауков?',
'номер самого электроотрицательного элемента'
]
def main():
    right = 0
    lose = 0
    pygame.init()
    clock = pygame.time.Clock()
    sc = pygame.display.set_mode((WW, WH))
    pygame.display.set_caption("ЦИФРЫ")
    sc.fill(BLUE)
    pygame.draw.rect(sc, GREEN, (0, 300, 1000, 200))
    pygame.draw.circle(sc, YELLOW, (550, 100), 70)
    pygame.draw.rect(sc, WHITE, (30, 400, 640, 50))
    f1 = pygame.font.Font(None, 30)
    f2 = pygame.font.Font(None, 22)
    num = randint(0, 9)
    s1 = zadanie[num]
    text = f1.render(s1, 1, (BLACK))
    sc.blit(text, (60, 415))
    tright = f2.render('Правильно: ' + str(right), 1, (BLACK))
    tlose = f2.render('Неправильно: ' + str(lose), 1, (BLACK))
    sc.blit(tright, (450, 410))
    sc.blit(tlose, (450, 430))
    X = [70, 280, 480, 650]
    Y = [randint(-100, -40) for _ in range(4)]
    C = [randint(0,9) for _ in range(4)]
    pygame.display.update()
    while lose < 3:
        sc.fill(BLUE)
        pygame.draw.rect(sc, GREEN, (0, 300, 1000, 200))
        pygame.draw.circle(sc, YELLOW, (550, 100), 70)
        for i in range(4):  pygame.draw.circle(sc, CORAL, [X[i], Y[i]], radius + 4)
        for i in range(4):  pygame.draw.circle(sc, WHITE, [X[i], Y[i]], radius)
        TC = [f1.render(str(C[i]), 1, BLACK) for i in range(4)]
        for i in range(4): sc.blit(TC[i], (X[i]-5, Y[i]-11))
        pygame.draw.rect(sc, WHITE, (30, 400, 640, 50))
        text = f1.render(s1, 1, (BLACK))
        sc.blit(text, (60, 415))
        tright = f2.render('Правильно: ' + str(right), 1, (BLACK))
        tlose = f2.render('Ошибок: ' + str(lose), 1, (BLACK))
        sc.blit(tright, (450, 410))
        sc.blit(tlose, (450, 430))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.MOUSEBUTTONDOWN and i.button:
                for u in range(4):
                    if (i.pos[0] - X[u]) ** 2 + (i.pos[1] - Y[u]) ** 2 <= 1600:
                        if C[u] == num:
                            right += 1
                            C[u] = 'Ура!'
                            num = randint(0, 9)
                            s1 = zadanie[num]
                        else:
                            lose += 1
        if lose >= 3:
            pygame.draw.rect(sc, PINK, (230, 210, 200, 100))
            pygame.draw.rect(sc, YELLOW2, (250, 270, 60, 30))
            loset=f2.render('Проигрыш(((', 1, (WHITE))
            new=f2.render('Заново', 1, (BLACK))
            sc.blit(loset, (240, 240))
            sc.blit(new, (255, 276))
            for i in pygame.event.get():
                if i.type == pygame.MOUSEBUTTONDOWN and i.button:
                    if i.pos[0] > 250 and i.pos[0] < 310 and i.pos[1] > 270 and i.pos[1] < 300:
                        main()
        clock.tick(FPS)
        pygame.display.update()
        Y = [i + 1 for i in Y]
        for i in range(4):
            if Y[i] == 500:
                if C[i] == num: lose += 1
                Y[i] = randint(-100, -40)
                C[i] = randint(0, 9)
main()
