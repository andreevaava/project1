import pygame, random

FPS = 60
WW=700
WH=500
BLACK = (15, 0, 0)
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 255, 127)
YELLOW = (255, 255, 0)
PINK = (235, 108, 163)
YELLOW2 = (238, 247, 107)
CORAL = (255, 127, 80)
radius = 40
def zadanie(a):
    if a == 0:
        s = 'Сколько костей в языке?'
    elif a == 1:
        s = 'Сколько пар жабр у человека на стадии эмбриона?'
    elif a == 2:
        s = 'Cколько дней живет муха?'
    elif a == 3:
        s = 'Cколько микротрубочек в триплете?'
    elif a == 4:
        s = 'Сколько стадий в митозе?'
    elif a == 5:
        s = 'Сколько царств по Уиттекеру'
    elif a == 6:
        s =  'кол-во ходильных конечностей у насекомых?'
    elif a == 7:
        s = 'pH нейтральной среды'
    elif a == 8:
        s = 'Сколько ходильных конечностей у паукообразных?'
    elif a == 9:
        s = 'номер самого электроотрицательного элемента'
    return(s)
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
    num = random.randint(0,9)
    s1 = zadanie(num)
    text = f1.render(s1, 1, (BLACK))
    sc.blit(text, (60, 415))
    tright = f2.render('Правильно: ' + str(right), 1, (BLACK))
    tlose = f2.render('Неправильно: ' + str(lose), 1, (BLACK))
    sc.blit(tright, (450, 410))
    sc.blit(tlose, (450, 430))
    x1 = 70
    x2 = 280
    x3 = 480
    x4 = 650
    y1 = random.randint(-100, -40)
    y2 = random.randint(-100, -40)
    y3 = random.randint(-100, -40)
    y4 = random.randint(-100, -40)
    c1 = random.randint(0,9)
    c2 = random.randint(0,9)
    c3 = random.randint(0,9)
    c4 = random.randint(0,9)
    pygame.display.update()
    while 1:
        if lose>=3:
            break
        sc.fill(BLUE)
        pygame.draw.rect(sc, GREEN, (0, 300, 1000, 200))
        pygame.draw.circle(sc, YELLOW, (550, 100), 70)
        pygame.draw.circle(sc, CORAL, [x1, y1], radius+4)
        pygame.draw.circle(sc, CORAL, [x2, y2], radius+4)
        pygame.draw.circle(sc, CORAL, [x3, y3], radius+4)
        pygame.draw.circle(sc, CORAL, [x4, y4], radius+4)
        pygame.draw.circle(sc, WHITE, [x1, y1], radius)
        pygame.draw.circle(sc, WHITE, [x2, y2], radius)
        pygame.draw.circle(sc, WHITE, [x3, y3], radius)
        pygame.draw.circle(sc, WHITE, [x4, y4], radius)
        tc1 = f1.render(str(c1), 1, BLACK)
        tc2 = f1.render(str(c2), 1, BLACK)
        tc3 = f1.render(str(c3), 1, BLACK)
        tc4 = f1.render(str(c4), 1, BLACK)
        sc.blit(tc1, (x1-5, y1-11))
        sc.blit(tc2, (x2-5, y2-11))
        sc.blit(tc3, (x3-5, y3-11))
        sc.blit(tc4, (x4-5, y4-11))
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
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if (i.pos[0]-x1)**2+(i.pos[1]-y1)**2<=1600:
                        if c1==num:
                            right+=1
                            c1 = str(c1)
                            c1 = 'Ура!'
                        else:
                            lose+=1
                    elif (i.pos[0]-x2)**2+(i.pos[1]-y2)**2<=1600:
                        if c2==num:
                            right+=1
                            c2 = str(c2)
                            c2 = 'Ура!'
                        else:
                            lose+=1
                    elif (i.pos[0]-x3)**2+(i.pos[1]-y3)**2<=1600:
                        if c3==num:
                            right+=1
                            c3 = str(c3)
                            c3 = 'Ура!'
                        else:
                            lose+=1
                    elif (i.pos[0]-x4)**2+(i.pos[1]-y4)**2<=1600:
                        if c4==num:
                            right+=1
                            c4 = str(c4)
                            c4 = 'Ура!'
                        else:
                            lose+=1
        if lose >= 3:
            pygame.draw.rect(sc, PINK, (230, 210, 200, 100))
            pygame.draw.rect(sc, YELLOW2, (250, 270, 60, 30))
            loset=f2.render('Проигрыш(((', 1, (WHITE))
            new=f2.render('Заново', 1, (BLACK))
            sc.blit(loset, (240, 240))
            sc.blit(new, (255, 276))
            while 1:
                for i in pygame.event.get():
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if i.button == 1:
                            if i.pos[0] > 250 and i.pos[0] < 310 and i.pos[1] > 270 and i.pos[1] < 300:
                                main()
                break
        clock.tick(FPS)
        pygame.display.update()
        y1+=1
        y2+=1
        y3+=1
        y4+=1
        if y1==500:
            if c1==num:
                lose+=1
            y1 = random.randint(-100, -40)
            c1 = random.randint(0,9)
        if y2==500:
            if c2==num:
                lose+=1
            y2 = random.randint(-100, -40)
            c2 = random.randint(0,9)
        if y3==500:
            if c3==num:
                lose+=1
            y3 = random.randint(-100, -40)
            c3 = random.randint(0,9)
        if y4==500:
            if c4==num:
                lose+=1
            y4 = random.randint(-100, -40)
            c4 = random.randint(0,9)

main()
